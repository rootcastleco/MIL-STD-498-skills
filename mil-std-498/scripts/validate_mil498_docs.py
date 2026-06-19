#!/usr/bin/env python3
"""Validate generated MIL-STD-498 style Markdown skeletons for expected headings."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, List

EXPECTED: Dict[str, List[str]] = {
    "SRS": ["Scope", "Referenced documents", "Functional requirements", "Requirements traceability"],
    "SDD": ["Scope", "Referenced documents", "Architecture", "Component", "traceability"],
    "STD": ["Scope", "Referenced documents", "Test case", "Expected results", "traceability"],
    "STR": ["Scope", "Referenced documents", "Execution", "Results", "risk"],
    "STP": ["Scope", "Referenced documents", "Test objectives", "Test strategy", "Entry and exit criteria"],
    "SVD": ["Scope", "Referenced documents", "Release", "Delivered files", "Known problems"],
    "SPS": ["Scope", "Referenced documents", "Product", "inventory", "Build"],
    "SUM": ["Scope", "Referenced documents", "Audience", "Task", "troubleshooting"],
    "ICD": ["Scope", "Referenced documents", "Controlled interface", "baseline", "Change control"],
}

CODE_RE = re.compile(r"^#\s+([A-Z0-9]+)\s+-", re.MULTILINE)


def inspect_file(path: Path) -> Dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = CODE_RE.search(text)
    code = match.group(1) if match else path.stem.split("-")[0].upper()
    expected = EXPECTED.get(code, ["Scope", "Referenced documents", "Tailoring", "Traceability"])
    missing = [item for item in expected if item.lower() not in text.lower()]
    tbd_count = text.count("[TBD")
    return {
        "file": str(path),
        "did": code,
        "missing_expected_terms": missing,
        "tbd_count": tbd_count,
        "status": "pass" if not missing else "review",
    }


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_mil498_docs.py <folder>", file=sys.stderr)
        return 2
    root = Path(argv[1]).expanduser().resolve()
    if not root.exists():
        print(f"Folder not found: {root}", file=sys.stderr)
        return 2
    files = sorted(root.glob("*.md"))
    report = {"root": str(root), "files_checked": len(files), "results": [inspect_file(path) for path in files]}
    print(json.dumps(report, indent=2))
    return 1 if any(result["missing_expected_terms"] for result in report["results"]) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
