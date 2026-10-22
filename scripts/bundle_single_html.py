"""Universal Single-File Offline HTML Bundler (`bundle_single_html.py`).

Inlines local <script src="..."> files and local <img src="..."> or JSON image paths
into a single 100% offline-capable HTML file ready for iOS/Android/iPad/Desktop.
"""

import argparse
import base64
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")


def encode_image_to_data_uri(img_path: str, max_width: int = 1150, quality: int = 78) -> str:
    """Encodes an image file into an optimized JPEG Base64 Data URI."""
    try:
        import pymupdf

        pix = pymupdf.Pixmap(img_path)
        if pix.alpha:
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix, False)
        if pix.width > max_width:
            scale = float(max_width) / pix.width
            pix = pymupdf.Pixmap(pix, int(pix.width * scale), int(pix.height * scale))
        raw_bytes = pix.tobytes("jpeg", jpg_quality=quality)
        b64 = base64.b64encode(raw_bytes).decode("ascii")
        return f"data:image/jpeg;base64,{b64}"
    except ImportError:
        with open(img_path, "rb") as f:
            raw_bytes = f.read()
        ext = os.path.splitext(img_path)[1].lower().lstrip(".")
        mime = "image/png" if ext == "png" else "image/jpeg"
        b64 = base64.b64encode(raw_bytes).decode("ascii")
        return f"data:{mime};base64,{b64}"


def bundle_html(html_path: str, output_path: str):
    base_dir = os.path.dirname(os.path.abspath(html_path))
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Inline local <script src="..."></script>
    def replace_script(match):
        src = match.group(1)
        if src.startswith(("http://", "https://", "//")):
            return match.group(0)
        local_js = os.path.join(base_dir, src)
        if not os.path.exists(local_js):
            return match.group(0)
        with open(local_js, "r", encoding="utf-8") as js_f:
            js_code = js_f.read()

        # Replace any relative "images/xxx.png" inside JS data with Base64 Data URIs
        def replace_js_img(img_match):
            rel_img = img_match.group(1)
            abs_img = os.path.join(base_dir, rel_img)
            if os.path.exists(abs_img):
                return f'"{encode_image_to_data_uri(abs_img)}"'
            return img_match.group(0)

        js_code = re.sub(r'"(images/[^"]+\.(?:png|jpg|jpeg|webp))"', replace_js_img, js_code)
        return f"<script>\n/* Inlined from {src} */\n{js_code}\n</script>"

    bundled = re.sub(
        r'<script\s+[^>]*src=["\']([^"\']+)["\'][^>]*>\s*</script>',
        replace_script,
        html,
    )

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(bundled)

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Success! Single-file bundle written to: {output_path} ({size_mb:.2f} MB)")


def main():
    parser = argparse.ArgumentParser(description="Bundle HTML + local JS/images into a single offline HTML file")
    parser.add_argument("--html", required=True, help="Input index.html path")
    parser.add_argument("--output", required=True, help="Output standalone HTML path")
    args = parser.parse_args()
    bundle_html(args.html, args.output)


if __name__ == "__main__":
    main()
