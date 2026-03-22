"""Convert CO-012 HTML to PDF using Playwright."""
from pathlib import Path
from playwright.sync_api import sync_playwright

folder = Path(__file__).resolve().parent
html_path = folder / "CO-012_Front_Entry_Door.html"
pdf_path = folder / "CO-012_Front_Entry_Door.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{html_path.as_posix()}")
    page.pdf(
        path=str(pdf_path),
        format="Letter",
        margin={"top": "20mm", "right": "15mm", "bottom": "20mm", "left": "15mm"},
        print_background=True,
    )
    browser.close()

print(f"Saved: {pdf_path}")
