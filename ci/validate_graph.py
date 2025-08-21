#!/usr/bin/env python3
"""
validate_graph.py - Validate the process graph for basic structural integrity.

This script reads `.process/graph.yaml` from the repository root and verifies:

* All node IDs are unique.
* Each node has a recognized kind (`activity`, `decision`, `gate`).
* Activities have a single `next` pointing to an existing node.
* Decisions have a list of branches with valid target nodes.
* Gates have `pass` and `fail` destinations.
* All referenced nodes exist in the graph.

It is intentionally lightweight and avoids external dependencies beyond PyYAML.
"""
import sys
import os
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required to run this script. Please install it or modify the script to use a different parser.", file=sys.stderr)
    sys.exit(1)


def load_graph(graph_path: Path) -> dict:
    with graph_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate(graph: dict) -> int:
    nodes = graph.get("nodes", [])
    ids = set()
    errors = []
    # Build id set and check duplicates
    for node in nodes:
        node_id = node.get("id")
        if not node_id:
            errors.append("Node missing id: {}".format(node))
            continue
        if node_id in ids:
            errors.append(f"Duplicate node id: {node_id}")
        ids.add(node_id)
    # Validate node structure
    for node in nodes:
        node_id = node.get("id")
        kind = node.get("kind")
        if kind not in ("activity", "decision", "gate"):
            errors.append(f"Node {node_id} has invalid kind: {kind}")
            continue
        if kind == "activity":
            nxt = node.get("next")
            if not isinstance(nxt, str):
                errors.append(f"Activity {node_id} must have a single string 'next' field")
        elif kind == "decision":
            branches = node.get("next")
            if not isinstance(branches, list):
                errors.append(f"Decision {node_id} must have a list of branches in 'next'")
                continue
            for br in branches:
                if "when" not in br or "node" not in br:
                    errors.append(f"Decision {node_id} has branch missing 'when' or 'node': {br}")
        elif kind == "gate":
            # Gate requires 'pass' and 'fail'
            if not isinstance(node.get("pass"), str) or not isinstance(node.get("fail"), str):
                errors.append(f"Gate {node_id} must have 'pass' and 'fail' fields as strings")
    # Validate transitions point to existing nodes
    for node in nodes:
        node_id = node.get("id")
        kind = node.get("kind")
        if kind == "activity":
            nxt = node.get("next")
            if nxt and nxt not in ids:
                errors.append(f"Activity {node_id} points to unknown node {nxt}")
        elif kind == "decision":
            for br in node.get("next", []):
                target = br.get("node")
                if target not in ids:
                    errors.append(f"Decision {node_id} branch targets unknown node {target}")
        elif kind == "gate":
            for key in ("pass", "fail"):
                target = node.get(key)
                if target not in ids:
                    errors.append(f"Gate {node_id} {key} targets unknown node {target}")
    if errors:
        for e in errors:
            print(f"Error: {e}", file=sys.stderr)
        return 1
    print("Graph validation succeeded.")
    return 0


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    graph_path = repo_root / ".process" / "graph.yaml"
    if not graph_path.exists():
        print(f"Graph file not found at {graph_path}", file=sys.stderr)
        return 1
    graph = load_graph(graph_path)
    return validate(graph)


if __name__ == "__main__":
    sys.exit(main())