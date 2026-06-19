# MIL-STD-498 quality checklist

Use this for document reviews, readiness checks, and gap analysis. Return concrete findings rather than vague advice.

## Review severity

- **blocker**: likely prevents acceptance, verification, traceability, operation, or release decision.
- **major**: material ambiguity, missing content, or unverifiable claim that should be fixed before baseline.
- **minor**: clarity, consistency, formatting, or maintainability issue.
- **note**: improvement opportunity or optional tailoring point.

## Universal checks

1. Scope identifies system, subsystem, CSCI, version, users, and boundaries.
2. Referenced documents are listed with versions and dates.
3. Tailoring decisions are explicit.
4. Requirements/design/test identifiers are stable and unique.
5. Requirements are verifiable and avoid vague words such as fast, robust, easy, secure, or user-friendly without measurable criteria.
6. Assumptions, constraints, dependencies, and open issues are visible.
7. Safety, security, privacy, reliability, maintainability, and operational constraints are addressed or explicitly excluded.
8. Interfaces have owners, versions, error handling, timing, compatibility, and test evidence.
9. Test artifacts map to requirements and include expected results plus evidence to capture.
10. Release/product documents identify exact files, versions, dependencies, known issues, and rollback/installation notes.

## Traceability checks

Return a gap when any of these links are missing:

- stakeholder need -> SSS/SRS/IRS requirement
- SRS/IRS requirement -> SDD/IDD/DBDD design element
- requirement -> STP/STD test case
- STD test case -> STR result
- delivered file/version -> SPS/SVD entry
- interface version -> ICD/IDD/IRS and conformance test

## Requirements quality checks

A good requirement has:

- one subject and one required behavior
- observable trigger/condition if relevant
- measurable constraint or acceptance threshold
- verification method: inspection, analysis, demonstration, or test
- unique ID and source trace
- rationale when non-obvious

Bad:

```text
The gateway should be secure and fast.
```

Better:

```text
SW-SEC-012: The gateway shall reject unauthenticated MQTT publish requests before message persistence, verified by TC-SEC-012.
SW-PERF-004: The gateway shall process 1,000 telemetry messages per second with p95 end-to-end ingest latency <= 250 ms under the load profile in PERF-PROFILE-001, verified by TC-PERF-004.
```

## Review output table

Use this format:

| ID | Severity | Evidence | DID expectation | Impact | Recommended fix |
|---|---|---|---|---|---|
| F-001 | major | Section 4 has no verification method for SW-012. | SRS requirements should be verifiable and traceable to qualification. | Test coverage cannot be proven. | Add verification method and corresponding STD test case. |

## Acceptance criteria examples

- 100% of normative requirements have IDs and verification methods.
- 100% of interface messages/signals have owner, version, schema/format, error behavior, and compatibility rule.
- 100% of test cases map to one or more requirements and have expected results.
- 0 blocker findings remain before baseline.
- All delivered files in the release package are listed in SPS/SVD with version/checksum/build provenance where available.
