# Security Policy — LegionOS

This repository currently ships **documentation only**. There is no running service, no secrets store, and no production dependency surface.

## Reporting

Open a private advisory or an issue on this repository. Do not file exploit how-tos against unimplemented subsystems as if they were live.

## Scope

- In scope: claim language, documentation accuracy, future CI secrets hygiene.
- Out of scope until implemented: Kubernetes NetworkPolicies, payment-processor keys, agent sandbox escapes. Those items in `docs/security.md` are **design intent**, not deployed controls.

## Known issues

None on the current docs-only tree (Sweep-073 scan: no lockfile, no runtime, no open Dependabot alerts expected).
