# Software Design Description: Telemetry Gateway

Document ID: TG-SDD-001  
Status: Example  
Revision: 0.1.0

## 1. Scope

This Software Design Description defines the architecture and detailed design for the telemetry gateway.

## 2. Referenced documents

- `SRS.md`
- `STD.md`
- `traceability.csv`
- Threat model: [TBD]

## 3. Architecture overview

The gateway uses a ports-and-adapters architecture. Protocol-specific ingress adapters translate external messages into stable domain commands. Sink adapters translate normalized telemetry events into downstream delivery calls.

```text
[Devices]
   | MQTT / HTTPS
   v
[Ingress Adapters] --> [Validation Port] --> [Core Telemetry Domain] --> [Routing Port] --> [Sink Adapters]
                              |                         |
                              v                         v
                       [Schema Registry]        [Metrics / Logs / Traces]
```

## 4. Design constraints

- Keep the core domain independent from MQTT, HTTPS, database, and cloud provider SDKs.
- Add integrations through adapters, gateways, and feature flags.
- Make validation deterministic and testable without network dependencies.
- Treat observability as a contract, not an afterthought.

## 5. Component design

| Component | Responsibility | Requirement mapping |
|---|---|---|
| MQTT Adapter | Authenticate MQTT clients and convert packets into telemetry commands. | TG-SRS-FR-001, TG-SRS-IR-001 |
| HTTPS Adapter | Accept TLS-protected telemetry requests and convert them into telemetry commands. | TG-SRS-FR-001, TG-SRS-IR-002 |
| Schema Validator | Validate payloads against versioned schemas. | TG-SRS-FR-002, TG-SRS-FR-003 |
| Core Telemetry Domain | Normalize accepted telemetry and enforce routing decisions. | TG-SRS-FR-004 |
| Sink Adapter Layer | Deliver normalized events to downstream systems with retry-safe behavior. | TG-SRS-IR-003 |
| Observability Module | Emit logs, metrics, traces, health, and readiness signals. | TG-SRS-SR-003 |
| Feature Flag Gateway | Control adapter rollout and rollback. | TG-SRS-FR-005, TG-SRS-SR-004 |

## 6. Data design

Canonical event shape:

```json
{
  "event_id": "uuid",
  "device_id": "string",
  "source_adapter": "mqtt|https",
  "schema_version": "string",
  "observed_at": "rfc3339 timestamp",
  "received_at": "rfc3339 timestamp",
  "payload": {},
  "validation": {
    "status": "accepted|rejected",
    "schema_id": "string"
  }
}
```

## 7. Security design

- Enforce authentication in ingress adapters before parsing high-risk payload bodies.
- Apply least privilege to downstream sink credentials.
- Redact secrets before logs, metrics, traces, and rejection records.
- Rate-limit unauthenticated and malformed traffic.

## 8. Observability design

Required telemetry:

- `gateway_ingress_events_total`
- `gateway_rejected_events_total`
- `gateway_processing_latency_ms`
- `gateway_sink_delivery_failures_total`
- distributed trace span: `ingress.validate.route.deliver`
- structured log fields: `event_id`, `device_id_hash`, `source_adapter`, `schema_version`, `result`

## 9. Rollback and migration design

- New adapters start behind feature flags.
- Schema migrations are versioned and backward compatible for at least one release window.
- Sink delivery changes use dual-write or shadow-write mode before cutover when risk is high.
- Rollback must disable new adapters without redeploying core domain code.

## 10. Requirements-to-design traceability

See `traceability.csv`.

## 11. Open issues

- [TBD] Concrete schema registry implementation
- [TBD] Deployment platform
- [TBD] Target sink systems
