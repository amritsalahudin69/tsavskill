#!/usr/bin/env python3
"""Perform lightweight renderer-aware checks on a standalone HTML scene.

These source checks do not prove browser runtime, visual appearance, or motion.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Pattern


THREEJS_CHECKS: tuple[tuple[str, Pattern[str]], ...] = (
    (
        "Three.js scene construction",
        re.compile(r"\bnew\s+(?:(?:THREE|three)\s*\.\s*)?Scene\s*\("),
    ),
    (
        "camera construction",
        re.compile(
            r"\bnew\s+(?:(?:THREE|three)\s*\.\s*)?"
            r"(?:Perspective|Orthographic)Camera\s*\("
        ),
    ),
    (
        "WebGL renderer initialization",
        re.compile(r"\bnew\s+(?:(?:THREE|three)\s*\.\s*)?WebGLRenderer\s*\("),
    ),
    (
        "render invocation",
        re.compile(r"\.\s*render\s*\("),
    ),
    (
        "animation-loop indicator",
        re.compile(r"\brequestAnimationFrame\s*\(|\.\s*setAnimationLoop\s*\("),
    ),
)

CANVAS2D_CHECKS: tuple[tuple[str, Pattern[str]], ...] = (
    ("Canvas element", re.compile(r"<canvas\b", re.IGNORECASE)),
    (
        "Canvas 2D context",
        re.compile(r"\.\s*getContext\s*\(\s*(['\"])2d\1", re.IGNORECASE),
    ),
    (
        "Canvas drawing operation",
        re.compile(
            r"\.\s*(?:clearRect|fillRect|strokeRect|drawImage|putImageData|"
            r"fill|stroke|arc|lineTo|moveTo|rect)\s*\("
        ),
    ),
    (
        "Canvas animation-loop indicator",
        re.compile(r"\brequestAnimationFrame\s*\(|\bsetInterval\s*\("),
    ),
)

RESIZE_TRIGGER = re.compile(
    r"\bResizeObserver\b"
    r"|\bdevicePixelRatio\b"
    r"|\baddEventListener\s*\(\s*['\"]resize['\"]"
    r"|\bonresize\b",
    re.IGNORECASE,
)
CANVAS_SIZE_ASSIGNMENT = re.compile(
    r"\b(?:canvas|ctx\s*\.\s*canvas|context\s*\.\s*canvas)"
    r"\s*\.\s*(width|height)\s*=",
    re.IGNORECASE,
)
CANVAS_STYLE_SIZE_ASSIGNMENT = re.compile(
    r"\bcanvas\s*\.\s*style\s*\.\s*(?:width|height)\s*=",
    re.IGNORECASE,
)


def has_explicit_canvas_dimensions(canvas_tag: str, source: str) -> bool:
    has_width_attribute = re.search(
        r"\bwidth\s*=\s*(?:['\"][^'\"]+['\"]|[^\s>]+)", canvas_tag, re.IGNORECASE
    )
    has_height_attribute = re.search(
        r"\bheight\s*=\s*(?:['\"][^'\"]+['\"]|[^\s>]+)", canvas_tag, re.IGNORECASE
    )
    assigned_dimensions = {
        match.group(1).lower() for match in CANVAS_SIZE_ASSIGNMENT.finditer(source)
    }
    return bool(
        (has_width_attribute and has_height_attribute)
        or {"width", "height"}.issubset(assigned_dimensions)
    )


def has_canvas_css_sizing(source: str, canvas_tag: str) -> bool:
    inline_style = re.search(
        r"\bstyle\s*=\s*['\"]([^'\"]*)['\"]", canvas_tag, re.IGNORECASE
    )
    if inline_style and re.search(
        r"\b(?:width|height)\s*:", inline_style.group(1), re.IGNORECASE
    ):
        return True

    selectors = ["canvas"]
    canvas_id = re.search(r"\bid\s*=\s*['\"]([^'\"]+)['\"]", canvas_tag, re.IGNORECASE)
    if canvas_id:
        selectors.append(f"#{canvas_id.group(1)}")
    canvas_classes = re.search(
        r"\bclass\s*=\s*['\"]([^'\"]+)['\"]", canvas_tag, re.IGNORECASE
    )
    if canvas_classes:
        selectors.extend(
            f".{class_name}" for class_name in canvas_classes.group(1).split()
        )

    for selector in selectors:
        rule_pattern = re.compile(
            re.escape(selector) + r"\s*\{([^}]*)\}", re.IGNORECASE | re.DOTALL
        )
        for rule in rule_pattern.finditer(source):
            if re.search(r"\b(?:width|height)\s*:", rule.group(1), re.IGNORECASE):
                return True
    return False


def validate(path: Path, renderer: str) -> int:
    if not path.exists():
        print(f"FAIL: HTML file does not exist: {path}", file=sys.stderr)
        return 1
    if not path.is_file():
        print(f"FAIL: path is not a regular file: {path}", file=sys.stderr)
        return 1

    try:
        source = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        print(f"FAIL: cannot read UTF-8 HTML file {path}: {error}", file=sys.stderr)
        return 1

    failed = False
    checks = THREEJS_CHECKS if renderer == "threejs" else CANVAS2D_CHECKS
    for label, pattern in checks:
        if pattern.search(source):
            print(f"PASS: {label}")
        else:
            print(f"FAIL: missing {label}")
            failed = True

    if renderer == "canvas2d":
        canvas_tag_match = re.search(r"<canvas\b[^>]*>", source, re.IGNORECASE)
        if canvas_tag_match:
            has_resize_or_scaling = (
                has_canvas_css_sizing(source, canvas_tag_match.group(0))
                or bool(RESIZE_TRIGGER.search(source))
                or bool(CANVAS_STYLE_SIZE_ASSIGNMENT.search(source))
            )
            if has_resize_or_scaling:
                if has_explicit_canvas_dimensions(canvas_tag_match.group(0), source):
                    print("PASS: Canvas backing dimensions for declared resize/scaling")
                else:
                    print("FAIL: resize/scaling is declared without explicit Canvas backing dimensions")
                    failed = True
            else:
                print("INFO: no explicit Canvas resize/scaling setup detected; check not applicable")

    print(
        "Static structural checks only; browser runtime, visual appearance, and motion are not tested."
    )
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check basic structure for a standalone HTML scene renderer."
    )
    parser.add_argument(
        "--renderer",
        choices=("threejs", "canvas2d"),
        required=True,
        help="renderer used by the scene",
    )
    parser.add_argument("html_file", type=Path, help="path to the standalone HTML scene")
    arguments = parser.parse_args()
    return validate(arguments.html_file, arguments.renderer)


if __name__ == "__main__":
    raise SystemExit(main())
