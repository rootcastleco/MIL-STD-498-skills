---
name: mil-std-498
description: create, tailor, and review mil-std-498 style software lifecycle documentation. use when the user asks for defense-style or contract-style software documents, data item descriptions, dids, cdrl planning, requirements/design/test/user/release documents, or named artifacts such as sdp, srs, sss, sdd, dbdd, irs, idd, icd, stp, std, str, sum, svd, sps, ocd, sip, or strp. also use for traceability matrices, did selection, document skeleton generation, and compliance/readiness reviews against mil-std-498 conventions.
---

# MIL-STD-498 Documentation Assistant

## Purpose

Use this skill to create, tailor, and review MIL-STD-498 style software documentation. Treat MIL-STD-498 as a rigorous documentation and lifecycle framework; do not claim contractual compliance unless the user provides the controlling contract, CDRL, DID revision, and tailoring decisions.

## Operating rules

- Preserve the user's language for deliverables unless they request otherwise.
- Start every task by identifying the artifact type: DID selection/CDRL, new document, document review, traceability, or skeleton generation.
- If project facts are missing, make explicit assumptions and use `[TBD: ...]` placeholders instead of inventing facts.
- Maintain stable section numbers and requirements IDs so outputs can live in version control.
- For formal deliverables, include a compliance matrix or traceability section mapping content to DID intent.
- If a contract, CDRL, SOW, or customer DID conflicts with this skill, the provided source controls.
- Prefer documentation-as-code outputs: Markdown, CSV traceability, and review tables.

## Workflow decision tree

1. **Selecting deliverables or planning a CDRL?** Load `references/did-catalog.md` and `references/tailoring-and-cdrl.md`, then recommend a minimal, justified DID set.
2. **Creating a document?** Load `references/did-catalog.md` and `references/document-structures.md`; draft the document with sectioned Markdown and a traceability block.
3. **Reviewing an existing document?** Load `references/quality-checklist.md`; return findings as severity-tagged issues with evidence and fixes.
4. **Generating many skeletons?** Run `scripts/mil498_bootstrap.py` to create Markdown shells and a traceability CSV, then customize the generated files.
5. **Checking generated docs?** Run `scripts/validate_mil498_docs.py` against the document folder and fix missing expected headings.

## Output contracts

### DID selection / CDRL planning

Return:

```markdown
# MIL-STD-498 Deliverable Plan

## Assumptions
- ...

## Recommended DIDs
| DID | Title | Why needed | Tailoring notes | Delivery cadence |
|---|---|---|---|---|

## Exclusions
| DID | Reason excluded | Revisit trigger |
|---|---|---|

## Traceability spine
[Requirement source -> DID -> section -> verification artifact]

## Risks and controls
[Risk -> control]
```

### New document draft

Return:

```markdown
# [DID code] - [Document title]

Document ID: [TBD]
Version: 0.1
Status: Draft
Project/System: [name]
Prepared for: [TBD]
Prepared by: [TBD]

## 0. Tailoring and assumptions

## 1. Scope

## 2. Referenced documents

## 3. Body
[Use the relevant structure from references/document-structures.md]

## 4. Requirements/design/test traceability

## 5. Open issues
```

### Review findings

Return:

```markdown
# MIL-STD-498 Readiness Review

## Summary
[pass / conditional pass / fail]

## Findings
| ID | Severity | Evidence | DID expectation | Impact | Recommended fix |
|---|---|---|---|---|---|

## Missing traceability
| Source item | Expected link | Current state | Fix |
|---|---|---|---|
```

## Tooling

Use bundled scripts only when they materially reduce repetitive work:

- `scripts/mil498_bootstrap.py`: creates Markdown document skeletons for one or more DID codes and a traceability CSV.
- `scripts/validate_mil498_docs.py`: checks generated Markdown files for expected headings and emits a JSON report.

Example:

```bash
python scripts/mil498_bootstrap.py --project "Telemetry Gateway" --dids SRS SDD STD STR SVD --out ./mil498-docs
python scripts/validate_mil498_docs.py ./mil498-docs
```

## References

- Load `references/did-catalog.md` for DID codes, names, purposes, and selection triggers.
- Load `references/document-structures.md` for recommended document sections.
- Load `references/tailoring-and-cdrl.md` for CDRL planning, tailoring, and lifecycle profiles.
- Load `references/quality-checklist.md` for review, traceability, acceptance, and evidence criteria.
- Load `references/source-index.md` when the user asks where the skill content came from or needs upstream document locations.
