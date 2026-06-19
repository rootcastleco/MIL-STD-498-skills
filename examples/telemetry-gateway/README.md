# Telemetry Gateway MIL-STD-498 Example

This example shows a small documentation-as-code package for a telemetry gateway using MIL-STD-498-style artifacts.

## Included artifacts

- `SRS.md` — Software Requirements Specification skeleton with measurable requirements.
- `SDD.md` — Software Design Description skeleton with adapter/gateway isolation.
- `STD.md` — Software Test Description skeleton with verification coverage.
- `STR.md` — Software Test Report skeleton with evidence placeholders.
- `traceability.csv` — requirement-to-design-to-test mapping.

## Assumptions

- The telemetry gateway ingests device telemetry over MQTT or HTTPS.
- The core domain model must remain stable; integrations are isolated behind adapters.
- Security, observability, rollback, and migration are first-class acceptance criteria.
- This is an example, not contractual MIL-STD-498 compliance evidence.
