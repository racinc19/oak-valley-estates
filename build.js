// build.js — zero-dependency build system
// Reads src/pages/*.html, resolves @include directives from src/partials/,
// writes output to oak-valley-estates-pages/
//
// Directive format (in HTML comments):
//   <!-- @include _nav.html(active="page.html",refresh="fnName") -->
//   <!-- @include _nav.html(active="page.html") -->
//   <!-- @include _styles.css -->   (inside a CSS block)
//   /* @include _styles.css */      (inside a <style> block)

const fs   = require('fs');
const path = require('path');

const SRC_PAGES    = path.join(__dirname, 'src', 'pages');
const SRC_PARTIALS = path.join(__dirname, 'src', 'partials');
const OUT_DIR      = path.join(__dirname, 'oak-valley-estates-pages');

// ── Load partials once ────────────────────────────────────────────────────────
function loadPartial(name) {
  const p = path.join(SRC_PARTIALS, name);
  if (!fs.existsSync(p)) throw new Error(`Partial not found: ${p}`);
  return fs.readFileSync(p, 'utf8');
}

const NAV_PARTIAL    = loadPartial('_nav.html');
const STYLES_PARTIAL = loadPartial('_styles.css');

// ── Helpers ───────────────────────────────────────────────────────────────────

/** Parse key=value pairs from an @include argument string like: active="foo.html",refresh="doRefresh" */
function parseArgs(argStr) {
  const args = {};
  if (!argStr) return args;
  // match key="value" pairs
  const re = /(\w+)="([^"]*)"/g;
  let m;
  while ((m = re.exec(argStr)) !== null) {
    args[m[1]] = m[2];
  }
  return args;
}

/** Build the resolved nav HTML from the partial + per-page args */
function resolveNav(argStr) {
  const args = parseArgs(argStr || '');
  const activePage  = args.active  || '';
  const refreshFn   = args.refresh || '';

  let nav = NAV_PARTIAL;

  // 1. Mark the active link: find the <a href="ACTIVE"> inside .topnav-links and add class="active"
  if (activePage) {
    // Remove any existing class="active" first (clean slate)
    nav = nav.replace(/\s+class="active"/g, '');
    // Match only nav links (inside <div class="topnav-links">).
    // We split on the topnav-links open-tag so we only operate inside that block.
    const divMarker = '<div class="topnav-links">';
    const divIdx = nav.indexOf(divMarker);
    if (divIdx !== -1) {
      const before  = nav.slice(0, divIdx + divMarker.length);
      const linksBlock = nav.slice(divIdx + divMarker.length);
      const baseActive = activePage.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      // Add class="active" to the first matching href in the links block
      const fixed = linksBlock.replace(
        new RegExp(`(href="${baseActive}"(?:[^>]*?))(>)`),
        '$1 class="active"$2'
      );
      nav = before + fixed;
    }
  }

  // 2. Inject refresh button before </div></nav>
  if (refreshFn) {
    const btn = `  <button class="topnav-refresh" onclick="${refreshFn}()">&#8635; Refresh</button>\n`;
    nav = nav.replace('</div></nav>', btn + '</div></nav>');
  }

  return nav.trimEnd();
}

// ── Process a single template file ───────────────────────────────────────────
function processFile(templatePath) {
  let src = fs.readFileSync(templatePath, 'utf8');

  // 1. Resolve  /* @include _styles.css */  (CSS include inside <style>)
  src = src.replace(/\/\* @include _styles\.css \*\//g, STYLES_PARTIAL);

  // 2. Resolve  <!-- @include _nav.html(...) -->
  src = src.replace(
    /<!-- @include _nav\.html(?:\(([^)]*)\))? -->/g,
    (_match, argStr) => resolveNav(argStr)
  );

  return src;
}

// ── Main ──────────────────────────────────────────────────────────────────────
function build() {
  const files = fs.readdirSync(SRC_PAGES).filter(f => f.endsWith('.html'));
  let count = 0;

  for (const file of files) {
    const inPath  = path.join(SRC_PAGES, file);
    const outPath = path.join(OUT_DIR, file);

    try {
      const output = processFile(inPath);
      fs.writeFileSync(outPath, output, 'utf8');
      console.log(`  built: ${file}`);
      count++;
    } catch (err) {
      console.error(`  ERROR: ${file} — ${err.message}`);
      process.exit(1);
    }
  }

  console.log(`\nBuild complete: ${count} file(s) written to oak-valley-estates-pages/`);
}

build();
