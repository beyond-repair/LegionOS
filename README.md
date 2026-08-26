# LegionOS

**The Autonomous Company Operating System**

> "Tell LegionOS what company you want. Wake up to a deployed business."

LegionOS is a fully autonomous, programmable distributed system that transforms a high-level idea into a deployed, revenue-generating business with minimal human intervention. It treats the entire company lifecycle as a unified, self-optimizing workflow.

## Core Architecture: 5-Layer Holarchy

| Layer              | Role                                      | Key Components                                      | Technologies                     |
|--------------------|-------------------------------------------|-----------------------------------------------------|----------------------------------|
| **Founder Brain**  | Strategic arbiter (CEO/CFO)               | LLM reasoning + deterministic state machines, budget & ROI guards | LangGraph, Python, FastAPI      |
| **Builder Brain**  | Deterministic execution (CTO)             | Code generation, CI/CD, immutable infra             | FastAPI, Next.js, Docker, K8s   |
| **Growth Brain**   | Stochastic execution (CMO)                | Ad copy, SEO, landing pages, A/B testing, acquisition | Python, Stripe, Google Ads API  |
| **Operations Brain**| Day-2 loop (COO)                         | Billing, telemetry, support, scaling                | Stripe, Prometheus, Grafana     |
| **Agent Factory**  | Infinite extensibility                    | Dynamic domain agents, plugin system, sandboxing    | Python, Neo4j, Qdrant           |

**Company Knowledge Graph** (the moat): Neo4j (relationships) + Qdrant (vectors) with hard tenant isolation and optional differential-privacy sharing.

## Minimal Viable Autonomy (MVA) Phases

1. Founder Brain MVP – autonomous $1k spend decisions with ROI projection
2. Builder + Growth Integration – idea → first customer < 24 h
3. Operations Brain – Stripe + telemetry + 99.9 % uptime
4. Agent Factory – 3 custom agents handling 80 % of tasks
5. Knowledge Graph – queryable insights across 10k companies
6. Full Autonomy Test – 10 companies end-to-end, 70 % profitable in 30 days

## Repository Structure (Initial)

```
LegionOS/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── interfaces.md
│   └── security.md
├── brains/
│   ├── founder/
│   ├── builder/
│   ├── growth/
│   ├── operations/
│   └── agent_factory/
├── knowledge_graph/
│   ├── neo4j/
│   └── qdrant/
├── sandbox/
│   └── k8s/
└── mva/
    └── phase1/
```

## Status

**Version**: 0.1 (Architectural Baseline)  
**Created**: 2026-08-26  
**Governance**: ADL-SEEM v3.0

See `docs/` for detailed contracts, threat models, and open questions.
