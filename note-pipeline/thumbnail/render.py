"""noteサムネイルを生成する。

使い方:
  pip install -q playwright pillow
  python3 note-pipeline/thumbnail/render.py spec.json out.png

spec.json の例:
{
  "tag": "心の調子と働く #01",
  "title_html": "<em>100%</em>で働けない日の<br><u>仕事術</u>",
  "sub_html": "うつと付き合いながらGAFAMで働く私が、<br><b>AIに任せていること</b>",
  "theme": "pink"            # pink / sage / blue / sand（任意）
  "title_size": 64            # 任意。1行が長いときは56〜60に下げる
}
title_html では <em>=アクセント色, <u>=マーカー, <br>=改行 が使える。
"""
import json
import os
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
CHAR = HERE.parent / "assets" / "sena.png"
THEMES = {
    "pink": ("#D9877F", "#C96F67", "#F3D2CC"),
    "sage": ("#8FA88C", "#6E8A6B", "#DCE6D8"),
    "blue": ("#7F9BB8", "#5F7C9C", "#D8E2EE"),
    "sand": ("#C9A27A", "#A9825A", "#EFE1CF"),
}
CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
]


def main(spec_path, out_path):
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    accent, accent_dark, blob = THEMES[spec.get("theme", "pink")]
    html = (HERE / "template.html").read_text(encoding="utf-8")
    for key, val in {
        "{{ACCENT}}": accent,
        "{{ACCENT_DARK}}": accent_dark,
        "{{BLOB}}": blob,
        "{{TITLE_SIZE}}": str(spec.get("title_size", 64)),
        "{{CHAR_SRC}}": CHAR.as_uri(),
        "{{TAG}}": spec["tag"],
        "{{TITLE_HTML}}": spec["title_html"],
        "{{SUB_HTML}}": spec["sub_html"],
    }.items():
        html = html.replace(key, val)

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        tmp = f.name
    exe = next((p for p in CHROME_CANDIDATES if os.path.exists(p)), None)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 670}, device_scale_factor=2)
        page.goto(Path(tmp).as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(1500)
        page.screenshot(path=out_path)
        browser.close()
    os.unlink(tmp)
    print(out_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
