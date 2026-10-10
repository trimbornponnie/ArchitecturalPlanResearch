"""Small looks at downloaded files for research agents: text and image counts of PDF pages, page renders and
contact sheets as JPEG (quality 75, long side <= 1400 px, about 300 kB at most), so an agent can view many
pages without large PNG payloads (incident 2026-10-01: agents stalled after ~33 PNG reads of ~1 MB).

    PY=python3   (Windows: py -3; run from the repository root)
    $PY tools/peek.py pdf-text  <file.pdf> [--pages 1-40] [--grep "pianta|sezione|Giudecca"]
    $PY tools/peek.py pdf-pages <file.pdf> --pages 12,13 --out <dir> [--long 1400]
    $PY tools/peek.py sheet     <file.pdf | image ...> --out <file.jpg> [--pages 1-24] [--cols 4]
    $PY tools/peek.py info      <image or pdf ...>
"""
import argparse
import re
import sys
from pathlib import Path

import pymupdf
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None


def page_list(spec, n):
    if not spec:
        return list(range(1, n + 1))
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), min(int(b), n) + 1))
        elif part.strip():
            out.append(int(part))
    return [p for p in out if 1 <= p <= n]


def save_jpeg(im, path, long=1400, limit=300_000):
    im = im.convert("RGB")
    if max(im.size) > long:
        im.thumbnail((long, long))
    q = 75
    while True:
        im.save(path, "JPEG", quality=q, optimize=True)
        if Path(path).stat().st_size <= limit or q <= 35:
            break
        q -= 10


def render(doc, pno, long):
    page = doc[pno - 1]
    zoom = long / max(page.rect.width, page.rect.height)
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("pdf-text")
    t.add_argument("pdf")
    t.add_argument("--pages")
    t.add_argument("--grep")
    t.add_argument("--chars", type=int, default=600)
    pp = sub.add_parser("pdf-pages")
    pp.add_argument("pdf")
    pp.add_argument("--pages", required=True)
    pp.add_argument("--out", required=True)
    pp.add_argument("--long", type=int, default=1400)
    s = sub.add_parser("sheet")
    s.add_argument("files", nargs="+")
    s.add_argument("--out", required=True)
    s.add_argument("--pages")
    s.add_argument("--cols", type=int, default=4)
    i = sub.add_parser("info")
    i.add_argument("files", nargs="+")
    c = sub.add_parser("crop", help="a part of an image at full resolution, e.g. a title block")
    c.add_argument("image")
    c.add_argument("--box", required=True, help="x0,y0,x1,y1 as fractions 0..1 of width and height")
    c.add_argument("--out", required=True)
    c.add_argument("--long", type=int, default=1400)
    a = ap.parse_args()

    if a.cmd == "crop":
        x0, y0, x1, y1 = [float(v) for v in a.box.split(",")]
        with Image.open(a.image) as im:
            w, h = im.size
            part = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
            save_jpeg(part, a.out, a.long)
            print(a.out, "%dx%d crop of %dx%d" % (part.width, part.height, w, h))
        return

    if a.cmd == "pdf-text":
        with pymupdf.open(a.pdf) as doc:
            print("%s: %d pages" % (a.pdf, doc.page_count))
            rx = re.compile(a.grep, re.I) if a.grep else None
            for p in page_list(a.pages, doc.page_count):
                page = doc[p - 1]
                txt = " ".join(page.get_text().split())
                imgs = page.get_images()
                draw = len(page.get_drawings()) if not rx else 0
                if rx and not rx.search(txt):
                    continue
                hits = sorted(set(m.group(0).lower() for m in rx.finditer(txt))) if rx else []
                print("--- page %d  images=%d%s%s" % (p, len(imgs), "" if rx else "  vector_paths=%d" % draw,
                                                    ("  hits=" + ",".join(hits)) if hits else ""))
                print(txt[:a.chars])
    elif a.cmd == "pdf-pages":
        out = Path(a.out)
        out.mkdir(parents=True, exist_ok=True)
        with pymupdf.open(a.pdf) as doc:
            for p in page_list(a.pages, doc.page_count):
                dest = out / ("%s_p%03d.jpg" % (Path(a.pdf).stem[:40], p))
                save_jpeg(render(doc, p, a.long), dest, a.long)
                print(dest)
    elif a.cmd == "sheet":
        tiles = []
        for f in a.files:
            if f.lower().endswith(".pdf"):
                with pymupdf.open(f) as doc:
                    for p in page_list(a.pages, doc.page_count)[:48]:
                        tiles.append((render(doc, p, 420), "%s p%d" % (Path(f).name[:28], p)))
            else:
                try:
                    with Image.open(f) as im:
                        im.thumbnail((420, 420))
                        tiles.append((im.convert("RGB"), "%s %dx%d" % (Path(f).name[:30], *Image.open(f).size)))
                except Exception as e:  # noqa: BLE001
                    print("skip %s: %s" % (f, e))
        cols = a.cols
        rows = (len(tiles) + cols - 1) // cols
        cell = 430
        sheet = Image.new("RGB", (cols * cell, rows * (cell + 18)), "white")
        d = ImageDraw.Draw(sheet)
        font = ImageFont.load_default()
        for k, (im, label) in enumerate(tiles):
            x, y = (k % cols) * cell, (k // cols) * (cell + 18)
            sheet.paste(im, (x + (cell - im.width) // 2, y + 18 + (cell - im.height) // 2))
            d.text((x + 4, y + 3), "%d %s" % (k + 1, label), fill="black", font=font)
        save_jpeg(sheet, a.out, long=1800, limit=350_000)
        print(a.out, "%d tiles" % len(tiles))
    elif a.cmd == "info":
        for f in a.files:
            try:
                if f.lower().endswith(".pdf"):
                    with pymupdf.open(f) as doc:
                        r = doc[0].rect
                        print("%s  pdf %d pages, first page %.0fx%.0f pt" % (f, doc.page_count, r.width, r.height))
                else:
                    with Image.open(f) as im:
                        print("%s  %s %dx%d %s dpi=%s" % (f, im.format, im.width, im.height, im.mode, im.info.get("dpi")))
            except Exception as e:  # noqa: BLE001
                print("%s  unreadable: %s" % (f, e))


if __name__ == "__main__":
    sys.exit(main())
