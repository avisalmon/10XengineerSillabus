"""Render the course flyers to A4 PDFs in downloads/.

Uses headless Edge or Chrome, whichever is installed. Run after editing
flyer.html or flyer-en.html:

    python tools\\build_pdfs.py
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "downloads")

FLYERS = [
    ("flyer.html", "10x-engineer-flyer-he.pdf"),
    ("flyer-en.html", "10x-engineer-flyer-en.pdf"),
]

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def find_browser():
    for path in BROWSERS:
        if os.path.exists(path):
            return path
    return None


def render(browser, source, target, profile):
    args = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--user-data-dir=" + profile,
        "--virtual-time-budget=6000",
        "--print-to-pdf=" + target,
        "file:///" + source.replace("\\", "/"),
    ]
    subprocess.run(args, timeout=120, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


def main():
    browser = find_browser()
    if not browser:
        print("no Edge or Chrome found, cannot render PDFs")
        return 1

    os.makedirs(OUT_DIR, exist_ok=True)
    for index, (html, pdf) in enumerate(FLYERS):
        source = os.path.join(ROOT, html)
        target = os.path.join(OUT_DIR, pdf)
        # each run needs its own profile directory, otherwise a second
        # headless instance attaches to the first one and never exits
        profile = os.path.join(ROOT, ".pdfprofile%d" % index)
        render(browser, source, target, profile)
        size = os.path.getsize(target) if os.path.exists(target) else 0
        print("%s -> downloads/%s (%d bytes)" % (html, pdf, size))

    for index in range(len(FLYERS)):
        profile = os.path.join(ROOT, ".pdfprofile%d" % index)
        if os.path.isdir(profile):
            import shutil
            shutil.rmtree(profile, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
