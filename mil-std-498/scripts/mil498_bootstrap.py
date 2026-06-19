#!/usr/bin/env python3
"""Generate MIL-STD-498 style Markdown skeletons and a traceability CSV."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Dict, List

DIDS: Dict[str, Dict[str, object]] = {
    "SDP": {"title": "Software Development Plan", "sections": ["Scope", "Referenced documents", "Project organization", "Development process", "Methods and tools", "Configuration management", "Quality assurance", "Security, safety, and risk management", "Schedule and resources", "Deliverables and CDRL mapping"]},
    "SIP": {"title": "Software Installation Plan", "sections": ["Scope", "Referenced documents", "Installation prerequisites", "Site preparation", "Installation package", "Installation procedure", "Rollback procedure", "Installation verification", "Risks and contingencies"]},
    "STRP": {"title": "Software Transition Plan", "sections": ["Scope", "Referenced documents", "Transition objectives", "Deliverables and repositories", "Training and knowledge transfer", "Support roles", "Open risks and defects", "Transition acceptance criteria"]},
    "OCD": {"title": "Operational Concept Description", "sections": ["Scope", "Referenced documents", "Current situation", "Proposed operational concept", "Users and roles", "Operational scenarios", "Operational environment", "Impacts and constraints", "Stakeholder-need traceability"]},
    "SSS": {"title": "System/Subsystem Specification", "sections": ["Scope", "Referenced documents", "System overview", "System requirements", "Interface requirements", "Qualification provisions", "Requirements traceability matrix", "Open issues"]},
    "SRS": {"title": "Software Requirements Specification", "sections": ["Scope", "Referenced documents", "CSCI overview", "Functional requirements", "Interface requirements", "Data requirements", "Performance requirements", "Security, safety, and quality requirements", "Qualification requirements", "Requirements traceability matrix", "Open issues"]},
    "IRS": {"title": "Interface Requirements Specification", "sections": ["Scope", "Referenced documents", "Interface identification", "Interface requirements", "Data/message requirements", "Timing and sequencing", "Error handling", "Security and safety", "Verification and traceability"]},
    "SSDD": {"title": "System/Subsystem Design Description", "sections": ["Scope", "Referenced documents", "System architecture", "Subsystem design", "Hardware/software allocation", "Modes and states", "Safety and security design", "Requirements-to-design traceability"]},
    "SDD": {"title": "Software Design Description", "sections": ["Scope", "Referenced documents", "CSCI-wide design decisions", "Architecture overview", "Component design", "Interface design summary", "Data design summary", "Error handling", "Security and safety design", "Requirements-to-design traceability"]},
    "DBDD": {"title": "Database Design Description", "sections": ["Scope", "Referenced documents", "Database overview", "Logical data model", "Physical schema", "Data dictionary", "Integrity and performance", "Security and retention", "Migration and rollback", "Requirements-to-data traceability"]},
    "IDD": {"title": "Interface Design Description", "sections": ["Scope", "Referenced documents", "Interface design overview", "Detailed data/message/API design", "Protocol and timing", "Error and state handling", "Versioning and compatibility", "Requirements-to-design traceability"]},
    "ICD": {"title": "Interface Control Document", "sections": ["Scope", "Referenced documents", "Controlled interface identification", "Participating systems and owners", "Interface baseline and version", "Physical/transport/protocol contract", "Data and semantic contract", "Change control", "Conformance tests", "Interface change log"]},
    "STP": {"title": "Software Test Plan", "sections": ["Scope", "Referenced documents", "Test objectives", "Test strategy", "Test environment", "Test levels and responsibilities", "Entry and exit criteria", "Requirements coverage approach", "Schedule and resources", "Risks and reporting"]},
    "STD": {"title": "Software Test Description", "sections": ["Scope", "Referenced documents", "Test case matrix", "Test procedures", "Test data", "Expected results", "Environment setup and teardown", "Requirements-to-test traceability"]},
    "STR": {"title": "Software Test Report", "sections": ["Scope", "Referenced documents", "Tested version", "Test environment", "Execution summary", "Results by test case", "Deviations and incidents", "Coverage and residual risk", "Conclusion"]},
    "SUM": {"title": "Software User Manual", "sections": ["Scope", "Referenced documents", "Audience and roles", "System overview", "Access prerequisites", "Task procedures", "Errors and troubleshooting", "Recovery and support", "Glossary"]},
    "SIOM": {"title": "Software Input/Output Manual", "sections": ["Scope", "Referenced documents", "I/O overview", "Input formats", "Output formats", "Operating procedures", "Error handling", "Examples"]},
    "SCOM": {"title": "Software Center Operator Manual", "sections": ["Scope", "Referenced documents", "Operator responsibilities", "Operating environment", "Startup and shutdown", "Monitoring and alarms", "Backup and recovery", "Troubleshooting", "Escalation"]},
    "COM": {"title": "Computer Operation Manual", "sections": ["Scope", "Referenced documents", "Computer/environment overview", "Operating procedures", "Controls and indicators", "Maintenance operations", "Fault handling", "Safety and security"]},
    "CPM": {"title": "Computer Programming Manual", "sections": ["Scope", "Referenced documents", "Programming environment", "Programming procedures", "Interfaces and APIs", "Build and debug", "Coding rules", "Examples"]},
    "FSM": {"title": "Firmware Support Manual", "sections": ["Scope", "Referenced documents", "Firmware environment", "Tools and programmers", "Programming procedure", "Verification procedure", "Recovery procedure", "Safety and configuration control"]},
    "SPS": {"title": "Software Product Specification", "sections": ["Scope", "Referenced documents", "Product identification", "Product inventory", "Build and reproduction instructions", "Dependencies", "Configuration baseline", "Third-party components", "Requirements/product traceability"]},
    "SVD": {"title": "Software Version Description", "sections": ["Scope", "Referenced documents", "Release identification", "Delivered files", "Changes since previous release", "Fixed defects", "Known problems", "Installation and rollback notes", "Build provenance", "Release recommendation"]},
}


def safe_filename(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_.-]+", "-", value.strip())
    return value.strip("-") or "document"


def document_markdown(project: str, code: str) -> str:
    data = DIDS[code]
    title = str(data["title"])
    sections: List[str] = list(data["sections"])  # type: ignore[arg-type]
    lines = [
        f"# {code} - {title}",
        "",
        "Document ID: [TBD]",
        "Version: 0.1",
        "Status: Draft",
        f"Project/System: {project}",
        "CSCI/Subsystem: [TBD if applicable]",
        "Prepared for: [TBD]",
        "Prepared by: [TBD]",
        "Date: [TBD: YYYY-MM-DD]",
        "",
        "## Revision history",
        "| Version | Date | Author | Change |",
        "|---|---|---|---|",
        "| 0.1 | [TBD] | [TBD] | Initial skeleton |",
        "",
        "## Tailoring statement",
        "[TBD: State which DID areas are included/excluded and why.]",
        "",
    ]
    for index, section in enumerate(sections, start=1):
        lines.extend([f"## {index}. {section}", "", "[TBD]", ""])
    lines.extend([
        "## Traceability notes",
        "",
        "| Source ID | Derived item | Section | Verification/evidence | Status |",
        "|---|---|---|---|---|",
        "| [TBD] | [TBD] | [TBD] | [TBD] | open |",
        "",
    ])
    return "\n".join(lines)


def write_traceability(out_dir: Path, project: str, dids: List[str]) -> None:
    path = out_dir / "traceability.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["project", "source_id", "requirement_or_need", "did", "section", "verification_artifact", "status", "notes"])
        for did in dids:
            writer.writerow([project, "TBD", "TBD", did, "TBD", "TBD", "open", "created by mil498_bootstrap.py"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate MIL-STD-498 style document skeletons.")
    parser.add_argument("--project", required=True, help="Project or system name")
    parser.add_argument("--dids", nargs="+", required=True, help="DID codes to generate, e.g. SRS SDD STD SVD")
    parser.add_argument("--out", required=True, help="Output directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    dids = [code.upper() for code in args.dids]
    unknown = [code for code in dids if code not in DIDS]
    if unknown:
        print(f"Unknown DID code(s): {', '.join(unknown)}")
        print(f"Known codes: {', '.join(sorted(DIDS))}")
        return 2

    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    for code in dids:
        filename = f"{code}-{safe_filename(str(DIDS[code]['title']))}.md"
        path = out_dir / filename
        if path.exists() and not args.force:
            print(f"Skip existing file: {path}")
            continue
        path.write_text(document_markdown(args.project, code), encoding="utf-8")
        print(f"Wrote {path}")
    write_traceability(out_dir, args.project, dids)
    print(f"Wrote {out_dir / 'traceability.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
