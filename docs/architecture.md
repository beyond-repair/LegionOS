# LegionOS Architecture

## 5-Layer Holarchy

See root README for high-level table.

### Data Flow
1. User idea → Founder Brain (plan + budget approval)
2. Founder → Builder Brain (code + deploy MVP)
3. Builder → Growth Brain (campaigns + acquisition)
4. Growth → Operations Brain (billing + telemetry + scaling)
5. All layers → Agent Factory (domain agents as needed)
6. All events → Company Knowledge Graph (feedback loop)

### Interface Contracts (v0.1)
- All inter-Brain communication via typed FastAPI + event bus (schema-enforced)
- Founder Brain is the sole authority for budget and ROI gates
- All agents run inside Docker/K8s sandboxes with NetworkPolicies and scoped keys

### Locked Invariants
- Clean layer separation
- Every spend decision requires ROI projection + budget circuit breaker
- Immutable infrastructure after deployment
- Hard tenant isolation by default
- No agent may exceed pre-approved financial or network scopes
