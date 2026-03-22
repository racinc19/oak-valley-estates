# Externalize base64 images from CO-005 HTML into separate files to reduce HTML size.
# Run from the CO-005 folder. Creates CO-005_images/ and overwrites CO-005_Rodriguez_AV_Upgrade.html.
import os
import re
import base64

CO_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(CO_DIR, "CO-005_Rodriguez_AV_Upgrade.html")
IMG_DIR = os.path.join(CO_DIR, "CO-005_images")
IMG_PREFIX = "co005"

def main():
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    os.makedirs(IMG_DIR, exist_ok=True)
    # Match src="data:image/TYPE;base64,DATA" (non-greedy until next ")
    pattern = re.compile(r'src="(data:image/(jpeg|png|gif);base64,([A-Za-z0-9+/=]+))"')
    idx = [0]

    def repl(m):
        full, mime_type, b64 = m.group(1), m.group(2), m.group(3)
        idx[0] += 1
        ext = "jpg" if mime_type == "jpeg" else mime_type
        name = f"{IMG_PREFIX}_{idx[0]:02d}.{ext}"
        path = os.path.join(IMG_DIR, name)
        try:
            data = base64.b64decode(b64)
            with open(path, "wb") as out:
                out.write(data)
        except Exception as e:
            print(f"Warning: could not decode image {name}: {e}")
        rel = f"CO-005_images/{name}"
        return f'src="{rel}"'

    new_html = pattern.sub(repl, html)
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Externalized {idx[0]} images to {IMG_DIR}. Updated {HTML_PATH}.")

if __name__ == "__main__":
    main()
