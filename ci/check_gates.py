#!/usr/bin/env python3
"""
check_gates.py - Verify that required artifacts exist for each gate.

This script scans the process graph for gate nodes and checks that each
`artifact` listed in a gate’s `requires` section exists in the repository.
It is a simplistic example of gate enforcement—real implementations should
also evaluate metrics and reviews via integration with your CI/CD and
monitoring systems.
"""
import sys
import os
from pathlib import Path
import yaml


def load_graph(graph_path: Path) -> dict:
    with graph_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_artifacts(repo_root: Path, gate: dict) -> list:
    missing = []
    for req in gate.get("requires", []):
        if isinstance(req, dict) and "artifact" in req:
            rel_path = req["artifact"]
            artifact_path = repo_root / rel_path
            if not artifact_path.exists():
                missing.append(rel_path)
    return missing


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    graph_path = repo_root / ".process" / "graph.yaml"
    if not graph_path.exists():
        print(f"Graph file not found at {graph_path}", file=sys.stderr)
        return 1
    graph = load_graph(graph_path)
    gates = [n for n in graph.get("nodes", []) if n.get("kind") == "gate"]
    any_missing = False
    for gate in gates:
        gate_id = gate.get("id")
        missing = check_artifacts(repo_root, gate)
        if missing:
            any_missing = True
            print(f"Gate {gate_id} missing artifacts:")
            for art in missing:
                print(f"  - {art}")
        else:
            print(f"Gate {gate_id} passed (all required artifacts present)")
    return 1 if any_missing else 0


if __name__ == "__main__":
    sys.exit(main())