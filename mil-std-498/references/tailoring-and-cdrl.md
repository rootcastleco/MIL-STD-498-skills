# Tailoring and CDRL planning

MIL-STD-498 is most useful when tailored. Do not generate every DID by default. Select the smallest defensible set that covers project risk, contract needs, interfaces, verification, and support.

## Tailoring principles

1. Start from risk and deliverable obligations, not from document volume.
2. Keep requirements, design, tests, and release evidence traceable.
3. Separate intent from format: Markdown is acceptable unless the user provides a required template.
4. Mark omitted sections explicitly with a rationale.
5. Keep CSCI-level content in SRS/SDD and system/subsystem-level content in SSS/SSDD.
6. Put interface requirements in IRS, detailed interface design in IDD, and cross-party controlled baselines in ICD.
7. For safety/security/regulatory projects, add domain-specific artifacts outside MIL-STD-498 as needed; do not force them into unrelated DIDs.

## Recommended DID sets by project profile

### Prototype or MVP with future hardening

Minimum: OCD, SRS, SDD, STD, SVD.
Optional: SDP, STP, SUM.

Why: captures concept, requirements, design, test cases, and version inventory without excessive ceremony.

### Production software product

Minimum: SDP, SRS, SDD, STP, STD, STR, SVD, SUM.
Optional: SPS, DBDD, IRS/IDD/ICD.

Why: covers lifecycle governance, requirements, design, verification, release, and user operation.

### Interface-heavy integration project

Minimum: OCD, SRS or SSS, IRS, IDD, ICD, STP, STD, STR, SVD.
Optional: SSDD, SDD, DBDD.

Why: controls interface requirements, design, versioning, conformance, and integration test evidence.

### Data platform or database-heavy system

Minimum: SRS, SDD, DBDD, STP, STD, STR, SVD.
Optional: SPS, SUM, IRS/IDD.

Why: emphasizes data schema, migration, performance, access control, and reproducibility.

### Safety/security/high-assurance software

Minimum: SDP, OCD, SSS, SRS, IRS, SSDD/SDD, STP, STD, STR, SVD, SPS.
Optional: IDD, ICD, DBDD, SUM, STRP.
Add separate hazard analysis, threat model, safety case, security case, SBOM, and vulnerability management artifacts as required.

Why: high assurance needs explicit planning, requirements, design, verification, product baseline, release evidence, and risk controls.

### Sustainment handoff

Minimum: SVD, SPS, STRP, SUM, SDD, STD/STR.
Optional: SDP, SIP, DBDD, ICD.

Why: focuses on reproducible product baseline, supportability, user guidance, and transition evidence.

## CDRL planning table fields

Use these fields when drafting a CDRL-like plan:

| Field | Guidance |
|---|---|
| Data item | DID code and title |
| Purpose | Why the customer/project needs it |
| Source obligations | SOW, contract clause, requirement source, or assumption |
| Tailoring | Included/excluded sections and rationale |
| Format | Markdown, PDF, DOCX, CSV, repository folder, or customer template |
| Delivery event | SDR, PDR, CDR, TRR, release, sprint milestone, acceptance, etc. |
| Frequency | One-time, per release, per build, on change, monthly, etc. |
| Review authority | Customer, QA, systems engineering, product owner, security, safety |
| Acceptance criteria | Measurable checks for complete and correct delivery |

## Traceability spine

Keep this chain visible:

```text
mission/stakeholder need -> system requirement -> software/interface requirement -> design element -> test case -> test result -> release/version evidence
```

Use stable identifiers:

- NEED-[nnn]
- SYS-[nnn]
- SW-[nnn]
- IF-[nnn]
- DES-[nnn]
- TC-[nnn]
- TR-[nnn]
- REL-[nnn]

## Tailoring statement template

```markdown
## Tailoring statement

This document follows MIL-STD-498 style DID intent for [DID code/title]. Sections were tailored as follows:

| DID area | Included? | Rationale | Evidence/location |
|---|---:|---|---|
| [area] | yes/no/partial | [why] | [section/link] |

Contractual note: [state whether a controlling CDRL/SOW was provided. If not, state that this is a project-template interpretation, not a compliance determination.]
```
