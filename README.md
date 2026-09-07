# LegionOS

**Classification:** RESEARCH  
**Claim level:** 0 (Idea) per [ADL-Governance CLAIM_VALIDATION](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)  
**Maturity:** 1 (architectural notes only)  
**Governance:** [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · ADL-SEEM v3.0

> This repository is an **unvalidated concept sketch**. It is not a deployed operating system, not a company, and not a revenue system. No autonomy, profitability, or uptime claim is evidenced.

## What exists today

- Root README (this file)
- `docs/architecture.md` — holarchy sketch (intent only)
- `docs/interfaces.md` — intended contracts (unimplemented)
- `docs/security.md` — intended threat model (unimplemented)
- `docs/open-questions.md` — unresolved design questions
- Docs-existence CI (does not prove product behavior)

## What does not exist

There is **no** Founder/Builder/Growth/Operations/Agent Factory implementation, no Knowledge Graph, no sandbox, no billing, no ads integration, no tenants, and no measured MVA phase.

The directory layout listed in earlier drafts (`brains/`, `knowledge_graph/`, `sandbox/`, `mva/`) is a **target sketch**, not a present tree.

## Intended architecture (unverified)

Concept-only 5-layer holarchy:

| Layer | Intended role | Implementation status |
|-------|---------------|------------------------|
| Founder Brain | Strategic / budget gates | Not implemented |
| Builder Brain | Code + deploy | Not implemented |
| Growth Brain | Acquisition | Not implemented |
| Operations Brain | Billing + telemetry | Not implemented |
| Agent Factory | Extensible agents | Not implemented |

Related OS-family sketches (also RESEARCH; do not treat any as canonical product):

- [RealityOS](https://github.com/beyond-repair/RealityOS)
- [Sovereign-OS](https://github.com/beyond-repair/Sovereign-OS)
- [SovereignOS](https://github.com/beyond-repair/SovereignOS)
- Mapping: [os-family-constitution-map](https://github.com/beyond-repair/os-family-constitution-map)

`Auto_Legion` is **SUPERSEDED** toward `sovereign-clean-room` (work-unit patterns), not a LegionOS runtime.

## Status

| Field | Value |
|-------|--------|
| Version | 0.1.3 (Sweep-095 re-confirm) |
| Created | 2026-08-26 |
| Last sweep | 2026-09-07 Sweep-095 |
| Tests / CI | Docs presence only (run **34036540383** success on `5d471c16`) |
| Releases / tags | none |
| Promotion to ACTIVE | Blocked until purpose, tests+CI for real modules, product SECURITY surface, and evidenced claim level ≥ engineering |

See `docs/` for contracts, threat-model notes, and open questions.
