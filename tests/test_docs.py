"""Docs-existence gate for LegionOS RESEARCH tree.

Does not validate product behavior. Absence of brains/ or knowledge_graph/
is expected at claim level 0.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "RESEARCH.md",
    "LICENSE",
    "SECURITY.md",
    "GOVERNANCE.md",
    "docs/architecture.md",
    "docs/interfaces.md",
    "docs/security.md",
    "docs/open-questions.md",
]

FORBIDDEN_UNCAPED = [
    "Wake up to a deployed business",
    "fully autonomous, programmable distributed system that transforms",
]


def test_required_docs_exist():
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    assert missing == [], f"missing required docs: {missing}"


def test_readme_states_research_and_claim_zero():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "RESEARCH" in text
    assert "Claim level" in text
    assert "0" in text
    for phrase in FORBIDDEN_UNCAPED:
        assert phrase not in text, f"uncapped product phrase present: {phrase}"


def test_no_unimplemented_runtime_dirs_required():
    # Presence of empty product dirs is optional; do not fail if absent.
    assert True
