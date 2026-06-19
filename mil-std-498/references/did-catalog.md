# MIL-STD-498 DID catalog

Use this file to select the right document type before drafting or reviewing. The core MIL-STD-498 public descriptions commonly list 22 Data Item Descriptions (DIDs). The VCTLabs repository also includes an ICD-related PDF; treat ICD as an interface-control companion artifact when the user asks for interface control rather than pure interface requirements or design.

## Quick selection rule

- Need project execution governance: SDP, SIP, STRP.
- Need concept and requirements: OCD, SSS, SRS, IRS.
- Need architecture and detailed design: SSDD, SDD, DBDD, IDD, optionally ICD.
- Need qualification testing: STP, STD, STR.
- Need user/operator information: SUM, SIOM, SCOM, COM.
- Need support/programming information: CPM, FSM.
- Need delivery/release/product definition: SPS, SVD.

## DID table

| Code | Title | Group | Use when | Typical primary traceability |
|---|---|---|---|---|
| SDP | Software Development Plan | Plan | Planning how software will be developed, managed, verified, configured, and delivered. | SOW/CDRL -> development activities -> milestones/evidence |
| SIP | Software Installation Plan | Plan | Planning installation at user or operational sites. | Deployment requirements -> site steps -> acceptance checks |
| STRP | Software Transition Plan | Plan | Planning transition from developer to support/maintenance agency. | Sustainment requirements -> support tasks -> handoff evidence |
| OCD | Operational Concept Description | Concept | Describing missions, users, operating modes, scenarios, constraints, and operational environment. | Stakeholder needs -> operational scenarios -> system requirements |
| SSS | System/Subsystem Specification | Requirements | Capturing requirements for a system or subsystem, not just a software CSCI. | Stakeholder/system requirements -> qualification methods |
| SRS | Software Requirements Specification | Requirements | Capturing requirements for a Computer Software Configuration Item (CSCI). | Source requirements -> software requirements -> verification |
| IRS | Interface Requirements Specification | Requirements | Capturing requirements imposed on one or more interfaces. | Interface needs -> interface requirements -> interface tests |
| SSDD | System/Subsystem Design Description | Design | Describing system/subsystem architecture and design decisions. | SSS requirements -> architecture/design elements |
| SDD | Software Design Description | Design | Describing software architecture and detailed design for a CSCI. | SRS requirements -> components/modules/interfaces/tests |
| DBDD | Database Design Description | Design | Describing database schema, data model, storage, access, integrity, and migration. | Data requirements -> schema objects -> tests/migrations |
| IDD | Interface Design Description | Design | Describing detailed design of one or more interfaces. | IRS requirements -> messages/APIs/protocols -> tests |
| ICD | Interface Control Document | Interface control companion | Controlling and versioning the agreed interface between systems/parties. Use when the user specifically asks for ICD or contract/interface control. | Interface baseline -> versions -> change control -> conformance tests |
| STP | Software Test Plan | Qualification test | Planning qualification testing strategy, environment, responsibilities, schedule, and pass/fail logic. | Requirements -> test strategy -> test resources |
| STD | Software Test Description | Qualification test | Writing test cases, procedures, test data, and expected results. | Requirements -> test cases/procedures -> results |
| STR | Software Test Report | Qualification test | Reporting executed tests, deviations, results, incidents, and analysis. | Test procedures -> observed results -> pass/fail evidence |
| SUM | Software User Manual | User/operator manual | Writing instructions for hands-on users. | User tasks -> procedures -> troubleshooting |
| SIOM | Software Input/Output Manual | User/operator manual | Documenting input/output for batch or center-operated systems. | Operational data flows -> formats -> procedures |
| SCOM | Software Center Operator Manual | User/operator manual | Documenting operator duties for a computer-center hosted system. | Operations tasks -> procedures -> monitoring |
| COM | Computer Operation Manual | User/operator manual | Documenting operation of the computer or computing environment. | Environment requirements -> operating procedures |
| CPM | Computer Programming Manual | Support manual | Documenting programming guidance for a computer or programmable system. | Support needs -> programming instructions |
| FSM | Firmware Support Manual | Support manual | Documenting firmware programming/support procedures. | Firmware support needs -> procedures -> tools |
| SPS | Software Product Specification | Product definition | Defining delivered executable, source, build, support files, and product baseline. | Product baseline -> files -> build/reproduction evidence |
| SVD | Software Version Description | Product definition | Describing the delivered version, inventory, changes, known issues, installation notes, and release status. | Change records -> release contents -> installation/known issues |

## Ambiguity handling

- If the user says "spec" without more detail, ask whether the scope is system/subsystem (SSS), software CSCI (SRS), interface requirements (IRS), product baseline (SPS), or version/release (SVD). If there is no time to ask, state the assumption.
- If the user asks for "test cases", produce STD by default; if they ask for test strategy, produce STP; if they ask for test results, produce STR.
- If the user asks for "architecture" or "design", choose SDD for software and SSDD for system/subsystem.
- If the user asks for API/protocol contract control across teams or vendors, choose ICD plus IRS/IDD as needed.
