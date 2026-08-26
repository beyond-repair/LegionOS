# LegionOS Security Baseline

## Sandboxing
- All agents and services run in isolated Docker containers orchestrated by Kubernetes.
- NetworkPolicies restrict egress to pre-approved endpoints only (Stripe, Google Ads, AWS, internal bus).

## API Key Management
- Scoped, time-limited (≤ 24 h), rate-limited keys.
- Example: Growth Brain Stripe key cannot charge > $100/day without Founder re-approval.

## Circuit Breakers
- Auto-pause after 3 consecutive failures.
- Exponential backoff on rate-limited APIs.

## Threat Model (Initial)
Simulate and neutralize:
- Rogue agents spinning up cryptominers
- Data exfiltration attempts
- API DDoS / abuse

Detection → Containment → Neutralization required before MVA Phase 4.

## Audit
Immutable, hash-chained logs of every decision and its rationale.
