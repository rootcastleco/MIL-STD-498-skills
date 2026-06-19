# MIL-STD-498 document structures

These are practical Markdown skeletons for MIL-STD-498 style outputs. They preserve DID intent without copying full source templates. Adapt sections to the provided CDRL/tailoring; otherwise keep sections and fill unknowns with `[TBD: ...]`.

## Universal front matter

Use this block for any formal document:

```markdown
# [DID] - [Title]

Document ID: [TBD]
Version: 0.1
Status: Draft
Project/System: [TBD]
CSCI/Subsystem: [TBD if applicable]
Prepared for: [TBD]
Prepared by: [TBD]
Date: [YYYY-MM-DD]

## Revision history
| Version | Date | Author | Change |
|---|---|---|---|

## Approval
| Role | Name | Approval/date |
|---|---|---|

## Tailoring statement
[State included/excluded sections, assumptions, and controlling sources.]
```

## SRS - Software Requirements Specification

1. Scope
2. Referenced documents
3. CSCI overview
4. Requirements
   - Functional requirements
   - External interface requirements
   - Internal interface requirements
   - Data requirements
   - Performance requirements
   - Security, privacy, and safety requirements
   - Reliability, availability, maintainability
   - Environmental, hardware, and resource constraints
   - Design and implementation constraints
   - Qualification requirements and acceptance criteria
5. Requirements traceability matrix
6. Notes, assumptions, and open issues

Requirement style:

```markdown
REQ-[area]-[nnn]: The software shall [observable behavior] when [condition], within [constraint], verified by [analysis/inspection/test/demo].
```

## SSS - System/Subsystem Specification

1. Scope and system/subsystem identification
2. Referenced documents
3. System overview and operational context
4. Requirements by capability, external interface, state/mode, data, performance, safety, security, and environment
5. Qualification provisions
6. Requirements traceability matrix
7. Notes and open issues

## OCD - Operational Concept Description

1. Scope
2. Referenced documents
3. Current system or situation
4. Justification for change or new capability
5. Proposed system concept
6. Users, roles, organizations, and responsibilities
7. Operational scenarios, states, modes, and workflows
8. External interfaces and operational environment
9. Impacts, risks, constraints, and support concept
10. Traceability to stakeholder needs

## SDP - Software Development Plan

1. Scope and software items
2. Referenced documents
3. Project organization and responsibilities
4. Development process, lifecycle, increments, and gates
5. Methods, tools, standards, coding rules, and documentation rules
6. Requirements, design, implementation, integration, and test approach
7. Configuration management and change control
8. Quality assurance, reviews, audits, and acceptance criteria
9. Security, safety, risk, and issue management
10. Schedules, milestones, resources, and dependencies
11. Data management, deliverables, and CDRL mapping
12. Supplier/subcontractor controls if applicable

## SDD - Software Design Description

1. Scope and CSCI identification
2. Referenced documents
3. CSCI-wide design decisions
4. Architecture overview
5. Component/module design
   - Purpose
   - Responsibilities
   - Inputs/outputs
   - State/data ownership
   - Error handling
   - Security and safety considerations
6. Interface design summary or links to IDD/ICD
7. Data design or links to DBDD
8. Requirements-to-design traceability
9. Design risks, alternatives, and rationale

## SSDD - System/Subsystem Design Description

1. Scope and system/subsystem identification
2. Referenced documents
3. System architecture and allocation of requirements
4. Subsystem/component design descriptions
5. Hardware/software/interface allocation
6. Operational modes and states
7. Safety, security, reliability, maintainability design decisions
8. Requirements-to-design traceability

## IRS, IDD, and ICD - Interface documents

For IRS:
1. Scope and interface identification
2. Referenced documents
3. Interface requirements
4. Message/API/signal/data requirements
5. Timing, sequencing, error handling, security, safety, and performance requirements
6. Verification and traceability

For IDD:
1. Scope and interface identification
2. Interface design overview
3. Detailed data/message/API/signal design
4. Protocol, timing, sequencing, state, and error design
5. Versioning and compatibility
6. Requirements-to-design traceability

For ICD:
1. Controlled interface identification
2. Participating systems/parties and ownership
3. Interface baseline and version
4. Physical, transport, protocol, data, and semantic contract
5. Compatibility, deprecation, and change-control rules
6. Conformance tests and acceptance evidence
7. Interface change log

## DBDD - Database Design Description

1. Scope and database identification
2. Referenced documents
3. Database overview and assumptions
4. Logical data model
5. Physical schema and storage design
6. Data dictionary
7. Integrity, constraints, indexing, and performance
8. Access control, security, privacy, audit, and retention
9. Backup, restore, migration, and rollback
10. Requirements-to-data traceability

## STP - Software Test Plan

1. Scope and test items
2. Referenced documents
3. Test objectives and strategy
4. Test environment, tools, simulators, and data
5. Test levels, types, and responsibilities
6. Entry/exit criteria and pass/fail rules
7. Requirements coverage approach
8. Schedule, resources, risks, and dependencies
9. Problem reporting and retest policy
10. Deliverables and reporting

## STD - Software Test Description

1. Scope
2. Referenced documents
3. Test case matrix
4. Test procedure details
5. Test data and expected results
6. Environment setup and teardown
7. Requirements-to-test traceability

Test case style:

```markdown
TC-[nnn]: [Title]
Requirement(s): REQ-...
Objective: ...
Preconditions: ...
Steps:
1. ...
Expected result: ...
Pass/fail criteria: ...
Evidence to capture: ...
```

## STR - Software Test Report

1. Scope and tested version
2. Referenced documents
3. Test environment actually used
4. Test execution summary
5. Results by test case
6. Deviations, incidents, defects, and waivers
7. Requirements coverage and residual risk
8. Conclusions and release recommendation

## SUM - Software User Manual

1. Scope and audience
2. Referenced documents
3. System overview
4. User roles, permissions, and safety/security notices
5. Installation/access prerequisites if relevant
6. Task-oriented procedures
7. Error messages, alarms, and troubleshooting
8. Recovery, backup, and support
9. Glossary and quick reference

## SPS - Software Product Specification

1. Scope and product identification
2. Referenced documents
3. Product inventory: binaries, source, configuration, scripts, data, documentation
4. Build and reproduction instructions
5. Dependencies, environment, and toolchain versions
6. Licensing, third-party components, and vulnerability notes
7. Configuration baseline and checksums
8. Requirements/product traceability

## SVD - Software Version Description

1. Scope and release identification
2. Referenced documents
3. Version inventory and media/files delivered
4. Changes since previous release
5. Fixed defects and known problems
6. Installation, upgrade, rollback, and compatibility notes
7. Operational limitations and residual risks
8. Build provenance and verification summary

## SIP - Software Installation Plan

1. Scope and installation sites
2. Referenced documents
3. Installation prerequisites and responsibilities
4. Installation package and media
5. Site preparation
6. Installation steps and rollback
7. Installation verification and acceptance
8. Risks, contingencies, and support

## STRP - Software Transition Plan

1. Scope and support target
2. Referenced documents
3. Transition objectives and schedule
4. Deliverables, repositories, environments, and access transfer
5. Training and knowledge transfer
6. Support roles, SLAs, and escalation
7. Open defects, risks, and technical debt
8. Acceptance criteria for transition complete
