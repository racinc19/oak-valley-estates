# AGENTS.md - Oak Valley Estates

This repo is a live project workspace for the Rodriguez Residence and related Oak Valley Estates site assets.

## Start here (future context)
- For OVE subs web edits, author in `Deploy/deploy_ovesubs`.
- The live `ovesubs.pages.dev` project is connected to GitHub `racinc19/ovesubs`, which publishes from `Deploy/site_ove` in that small repo.
- To ship OVE subs, run `Deploy/ship_ove_subs.ps1`; it copies `Deploy/deploy_ovesubs` into the local `ovesubs` clone at `Deploy/site_ove`, commits, and pushes the connected repo.
- Do not copy OVE subs files only to the root of the `ovesubs` repo; Cloudflare will not serve that root copy.
- Computer/browser automation lives outside this repo at `C:\Users\racin\Desktop\computer-control`; read `CONTEXT.md` there before saying desktop/Gmail/Sheets automation cannot be done.

## Primary role
When working here, act like a careful project operator for Rodriguez Residence.

Priorities:
1. Find the right project information quickly
2. Summarize documents clearly for Craig
3. Edit the correct deploy source folder when site changes are requested
4. Avoid casual renames, moves, or destructive cleanup

## Read first
If you are working on this repo, read these before making non-trivial changes:
- `Admin/Rodriguez_Agent.md`
- `Deploy/DEPLOY_OVE_SUBS_GIT.md` for OVE subs deployment
- `Deploy/DEPLOY_SOURCE.txt` for current site folder notes
- any directly relevant files in the target folder

## Source of truth
- Client site source of truth: `Deploy/deploy_live`
- OVE subs **authoring** in this monorepo: `Deploy/deploy_ovesubs` (edits go here; production deploys from a separate small repo, see `Deploy/DEPLOY_OVE_SUBS_GIT.md`)
- The Cloudflare `ovesubs` project is usually tied to GitHub **`racinc19/ovesubs`**, not this repo -- use `Deploy/ship_ove_subs.ps1` to copy + push that package
- Shared selections sync helper: `tools/sync_selections_to_ovesubs.mjs` (if present)

Do not edit generated or review copies when the live source folder is the real target.

### Archived folders (moved April 2026)
- `Archive/deploy_full_23_review/` -- stale review snapshot of deploy_full_23.zip; no longer in Deploy/
- `Archive/deploy_ovesubs_baseline/` -- frozen baseline of OVE subs at initial deploy; no longer in Deploy/

### Deploy/ root is clean
Loose HTML files (`index.html`, `budget.html`, `draws.html`, etc.) previously cluttering `Deploy/` root were removed -- they were older/duplicate copies of files in `deploy_live/` or `deploy_ovesubs/`. The only active site sources are `Deploy/deploy_live/` and `Deploy/deploy_ovesubs/`.

## Folder guide
- `Admin` → permits, vendor/admin records, project helper docs
- `Construction` → bids, contracts, change orders, project records, selections
- `Documents` → reference docs, plans, PDFs, source material
- `Trades` → trade-specific docs and working material
- `Deploy` → published site assets and deployment scripts
- `tools` → utility scripts for project content sync

## Working rules
- Treat this as production-adjacent work.
- Read before editing.
- Keep edits narrow and reversible.
- Prefer exact file paths in notes and summaries.
- If a request mentions Rodriguez/Rodrigues residence, assume this repo unless told otherwise.
- If changing shared site logic in `Deploy/deploy_live/shared.js`, sync the corresponding OVE subs copy after.
- Do not move or rename project files unless Craig explicitly asks.

## Common tasks
- locate project documents
- summarize change orders or selections
- prepare client or subcontractor updates
- determine whether a web edit belongs in `deploy_live` or `deploy_ovesubs`
- make small safe updates to the static site and deployment files

## Helpful commands
- OVE subs live deploy (copy `Deploy/deploy_ovesubs` → local `ovesubs` clone, push to `racinc19/ovesubs`): `Deploy/ship_ove_subs.ps1` — `Deploy/DEPLOY_OVE_SUBS_GIT.md`
- Direct upload only (bypasses Git; needs API token + Node): `Deploy/deploy_ovesubs.ps1`
- `npm run sync:selections` / `npm run deploy:live` / `npm run deploy:subs` / `npm run deploy` (if `package.json` is present in your clone)
