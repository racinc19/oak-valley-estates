# OVE subs: two repos (edit here → ship to GitHub `ovesubs` → Cloudflare)

There are **two** Git places involved:

| | |
|---|---|
| **This monorepo** (`oak-valley-estates`) | **Authoring** live code under **`Deploy/deploy_ovesubs`**. This is the folder we edit in the Oak Valley workspace. |
| **GitHub `racinc19/ovesubs`** | The repo **Cloudflare Pages is actually connected to** (what you see in the CF dashboard: `ove subs` → `racinc19/ovesubs`). Pushes to **`main`** (or your production branch) there trigger a deploy. |

**Cloudflare** does *not* build from the monorepo path `Deploy/deploy_ovesubs` unless you change the Pages project to the big repo. Today your dashboard points at **`ovesubs`**, so the way to go live is: get the monorepo folder’s contents into **`racinc19/ovesubs`**, then push **that** repo.

---

## Day-to-day: one command (no local Wrangler)

1. Work in **`Deploy/deploy_ovesubs`** in the Oak Valley repo.
2. Run:

   `powershell -File Deploy/ship_ove_subs.ps1`

The script copies into the **ove subs** GitHub package repo at **`Deploy/site_ove`**, which is the directory Cloudflare Pages uses for `ovesubs.pages.dev` (see `racinc19/ovesubs`’s `wrangler.toml`: `pages_build_output_dir = "./Deploy/site_ove"`). **Do not** rely on copying to the root of that repo for what the public site shows.

   The script will:
   - Copy **`Deploy/deploy_ovesubs`** into a local clone of **`https://github.com/racinc19/ovesubs`**
   - `git add` / `git commit` / `git push` in **that** clone (this is what starts the Cloudflare build)

**No Cloudflare API token** is required for this path — it’s just Git to GitHub.

**Clone location (pick one):**

- **Default:** same parent folder as this repo, named **`ovesubs`** (a sibling of `Oak-Valley-Estates`):

  ```text
  <parent>/
    Oak-Valley-Estates/     ← this monorepo
    ovesubs/                 ←  git clone https://github.com/racinc19/ovesubs
  ```

  The ship script will find it automatically if `.git` exists there.

- **Or** put any path in **`Deploy/ove_subs_sync_target.txt`** (one line; `#` = comment). See **`Deploy/ove_subs_sync_target.example.txt`**.

- **Or** pass **`-OveSubsPath`**.

**Optional**

- **`-AlsoPushSourceRepo`** — also commit and push the monorepo so GitHub has the same tree under `Deploy/deploy_ovesubs` (handy for backup / other collaborators).

- **`-WithWrangler`** — still runs **`deploy_ovesubs.ps1`** (direct `wrangler` upload) only for emergencies. Needs a token; normal life should not use it.

---

## Cloudflare (already correct if you use the ovesubs repo)

For the **ovesubs** Pages project connected to **`racinc19/ovesubs`**, typical static settings are:

- **Build command:** (empty)  
- **Build output directory:** **`/`** (repo root) or leave default **/** — the whole small repo is the static site, no subfolder.  
- **Branch:** the branch you push to (e.g. **`main`**)

You do **not** set build output to `Deploy/deploy_ovesubs` in that project — that path only exists in the monorepo.

If you later pointed Cloudflare at **`oak-valley-estates`**, you would set output to **`Deploy/deploy_ovesubs`** in that *different* Pages project — and you would not need the two-repo sync.

---

## If the ship script says it can’t find a clone

```powershell
cd <the folder ABOVE Oak-Valley-Estates>
git clone https://github.com/racinc19/ovesubs.git
```

Or clone anywhere, then set **`Deploy/ove_subs_sync_target.txt`** to that full path, or use **`-OveSubsPath`**.
