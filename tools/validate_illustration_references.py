"""Validate reference filenames, one manifest per entity/episode, and PNG inventory."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import zlib
from pathlib import Path


SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
EPISODE = r"(?:e(?!000)[0-9]{3}|s[0-9]+e[0-9]{2})"
PREFIX = rf"(?P<campaign>{SLUG})_(?P<entity>{SLUG})_(?P<episode>{EPISODE})"
IMAGE_NAME = re.compile(rf"{PREFIX}_(?P<role>{SLUG})_v(?P<version>[0-9]{{2}})\.png")
MANIFEST_NAME = re.compile(rf"{PREFIX}_manifest\.json")
DEFAULT_DIRECTORY = Path(__file__).resolve().parents[1] / "illustrations" / "references"


def png_metadata(path: Path) -> dict:
    """Read PNG chunks and the actual ICC profile without re-encoding the image."""
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("invalid PNG signature")
    position = 8
    result: dict = {
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "icc_profile": None,
    }
    seen_header = False
    seen_end = False
    while position < len(data):
        length = struct.unpack_from(">I", data, position)[0]
        tag = data[position + 4 : position + 8]
        end = position + 8 + length
        payload = data[position + 8 : end]
        stored_crc = struct.unpack_from(">I", data, end)[0]
        if zlib.crc32(tag + payload) & 0xFFFFFFFF != stored_crc:
            raise ValueError(f"bad {tag!r} chunk CRC")
        if tag == b"IHDR":
            width, height, depth, color, _, _, _ = struct.unpack(">IIBBBBB", payload)
            result.update(width=width, height=height, bit_depth=depth,
                          color_mode={0: "L", 2: "RGB", 3: "P", 4: "LA", 6: "RGBA"}[color])
            seen_header = True
        elif tag == b"iCCP":
            name, compressed = payload.split(b"\0", 1)
            if compressed[0] != 0:
                raise ValueError("unsupported ICC compression method")
            profile = zlib.decompress(compressed[1:])
            result["icc_profile"] = {
                "png_name": name.decode("latin-1"),
                "bytes": len(profile),
                "sha256": hashlib.sha256(profile).hexdigest(),
            }
        elif tag == b"IEND":
            seen_end = True
            if end + 4 != len(data):
                raise ValueError("data after PNG end")
            break
        position = end + 4
    if not seen_header or not seen_end:
        raise ValueError("missing PNG header or end")
    return result


def validate(directory: Path) -> tuple[list[str], int, int]:
    errors: list[str] = []
    claimed: set[str] = set()
    groups: set[tuple[str, str, str]] = set()
    manifest_count = 0
    if not directory.is_dir():
        return [f"Missing directory: {directory}"], 0, 0
    files = sorted(directory.iterdir())
    for path in files:
        if not path.is_file() or path.suffix not in {".png", ".json"}:
            errors.append(f"Unexpected reference entry: {path.name}")
            continue
        if path.suffix == ".png":
            match = IMAGE_NAME.fullmatch(path.name)
            if not match or int(match["version"]) < 1:
                errors.append(f"Invalid image filename: {path.name}")
            continue
        manifest_count += 1
        match = MANIFEST_NAME.fullmatch(path.name)
        if not match:
            errors.append(f"Invalid manifest filename: {path.name}")
            continue
        group = (match["campaign"], match["entity"], match["episode"])
        if group in groups:
            errors.append(f"Duplicate entity/episode: {group}")
        groups.add(group)
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
            if document["schema_version"] != 1:
                raise ValueError("unsupported manifest schema version")
            for field, expected in zip(("campaign", "entity", "episode"), group):
                if document[field] != expected:
                    raise ValueError(f"{field} disagrees with manifest filename")
            if not document["assets"]:
                raise ValueError("empty asset inventory")
            for asset in document["assets"]:
                name = asset["filename"]
                asset_match = IMAGE_NAME.fullmatch(name)
                if not asset_match or tuple(asset_match[f] for f in ("campaign", "entity", "episode")) != group:
                    raise ValueError(f"invalid or foreign asset filename: {name}")
                if int(asset_match["version"]) < 1:
                    raise ValueError(f"invalid version: {name}")
                if asset["role"] != asset_match["role"] or asset["version"] != int(asset_match["version"]):
                    raise ValueError(f"role/version disagrees with filename: {name}")
                if name in claimed:
                    raise ValueError(f"asset listed more than once: {name}")
                claimed.add(name)
                actual = png_metadata(directory / name)
                for field, value in actual.items():
                    if asset[field] != value:
                        errors.append(f"{name}: {field} differs from registered bytes")
        except (OSError, ValueError, KeyError, TypeError, IndexError, struct.error, zlib.error) as exc:
            errors.append(f"{path.name}: {exc}")
    images = {p.name for p in files if p.is_file() and p.suffix == ".png"}
    for name in sorted(images - claimed):
        errors.append(f"PNG missing from manifest: {name}")
    if not manifest_count:
        errors.append("No manifests found")
    return errors, manifest_count, len(images)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=DEFAULT_DIRECTORY)
    args = parser.parse_args()
    errors, manifests, images = validate(args.directory)
    for error in errors:
        print(error)
    print(f"Checked {images} PNGs and {manifests} entity/episode manifests; {len(errors)} error(s).")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
