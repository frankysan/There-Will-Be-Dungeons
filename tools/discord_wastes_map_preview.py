"""Create PRIVATE reduced previews for comparative review of Wastes cartography.

Output is local/discord/map-comparison-2026-10-27/, which is Git-ignored.
This helper reads original JPEG/WebP files but never alters them.
Requires Pillow (python -m pip install Pillow).
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import json

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError as error:
    raise SystemExit("Pillow is required: python -m pip install Pillow") from error

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "Beau-attributed Known Wastes (v3)": ROOT / "local/downloads/wastes/669709591344316416--The_Known_Wastes_Large_v3.jpg",
    "Beyond the Deadfingers": ROOT / "local/images-wiki/maps/Beyond the Deadfingers.webp",
    "Beyond the Deadfingers - annotated": ROOT / "local/images-wiki/maps/Beyond the Deadfingers - Annotated.webp",
    "The Teet and Trashburg": ROOT / "local/images-wiki/maps/The Teet and Trashburg.webp",
    "Slavetown": ROOT / "local/images-wiki/maps/Slavetown.webp",
    "Dusthill surface": ROOT / "local/images-wiki/maps/Dusthill.webp",
    "Dusthill caverns": ROOT / "local/images-wiki/maps/Dusthill Caverns.webp",
}
DEST = ROOT / "local/discord/map-comparison-2026-10-27"
CHARACTER_FILES = {
    "Stanley S1 miniature": ROOT / "local/downloads/wastes/738777012444856381--StanleyS1.png",
    "Stanley S2 miniature": ROOT / "local/downloads/wastes/738777095118782495--StanleyS2.png",
    "Evolution of Nash - undated fan art": ROOT / "local/downloads/wastes/672186714638254090--evolution-of-nash.jpg",
    "Vorel screenshot": ROOT / "local/downloads/wastes/761462415833038878--Vorel_screenshot.png",
    "Hope screenshot": ROOT / "local/downloads/wastes/761462418051301387--Hope_screenshot.png",
    "Nash screenshot": ROOT / "local/downloads/wastes/761462421486436363--Nash_Maggard_screenshot.png",
    "Stanley screenshot": ROOT / "local/downloads/wastes/761767030457630720--stanley_screenshot.png",
    "Diontalus screenshot": ROOT / "local/downloads/wastes/765592086245670922--diontalus_screenshot__1_.png",
}
EXPECTED_MAP_HASH = "cb014c6cad1ee98f59805ca71e74ceae07c05844cf1ee6e9244d871fad02d070"

def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for part in iter(lambda: f.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()

def card(label: str, image: Image.Image, width: int = 1440, height: int = 920) -> Image.Image:
    canvas = Image.new("RGB", (width, height), "#f3f0e8")
    draw = ImageDraw.Draw(canvas)
    draw.text((22, 22), label, fill="#222222")
    # Proportional scale; no crop, rotation or retouching of original source.
    picture = ImageOps.contain(image.convert("RGB"), (width - 44, height - 80), Image.Resampling.LANCZOS)
    canvas.paste(picture, ((width - picture.width) // 2, 58 + (height - 80 - picture.height) // 2))
    return canvas

def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    summary = []
    cards = []
    for label, path in FILES.items():
        digest = hash_file(path)
        if label.startswith("Beau-") and digest != EXPECTED_MAP_HASH:
            raise ValueError("Beau map does not match the archived checksum")
        with Image.open(path) as im:
            im.load()
            summary.append({
                "label": label, "path": str(path.relative_to(ROOT)),
                "format": im.format, "width": im.width, "height": im.height,
                "sha256": digest, "source_bytes": path.stat().st_size,
            })
            cards.append(card(label, im))
            if label.startswith("Beau-"):
                thumb = ImageOps.contain(im.convert("RGB"), (1440, 900), Image.Resampling.LANCZOS)
                thumb.save(DEST / "known-wastes-v3-preview.jpg", quality=84, optimize=True)
    width, height = cards[0].size
    board = Image.new("RGB", (width * 2, height * 4), "#f3f0e8")
    for index, c in enumerate(cards):
        board.paste(c, ((index % 2) * width, (index // 2) * height))
    board.save(DEST / "seven-map-contact-sheet.jpg", quality=83, optimize=True)
    character_cards = []
    for label, path in CHARACTER_FILES.items():
        with Image.open(path) as im:
            im.load()
            character_cards.append(card(label, im, width=580, height=620))
            summary.append({
                "label": label, "path": str(path.relative_to(ROOT)),
                "format": im.format, "width": im.width, "height": im.height,
                "sha256": hash_file(path), "source_bytes": path.stat().st_size,
                "classification": "Visual reference; not automatically episode-era canon",
            })
    portraits = Image.new("RGB", (580 * 4, 620 * 2), "#f3f0e8")
    for index, c in enumerate(character_cards):
        portraits.paste(c, ((index % 4) * 580, (index // 4) * 620))
    portraits.save(DEST / "character-reference-contact-sheet.jpg", quality=80, optimize=True)
    (DEST / "inventory.private.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "preview": str(DEST / "known-wastes-v3-preview.jpg"),
        "comparison": str(DEST / "seven-map-contact-sheet.jpg"),
        "maps_reviewed": len(summary), "source_files_untouched": True,
    }, indent=2))

if __name__ == "__main__":
    main()
