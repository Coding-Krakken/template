#!/usr/bin/env python3
"""
render_diagrams.py - Convert the process graph to a Mermaid flowchart.

Usage:
  python render_diagrams.py [--output path]

If an output file is provided, the Mermaid syntax will be written there;
otherwise it will be printed to stdout.  Mermaid diagrams can be rendered
using many tools (e.g. GitHub markdown, VS Code extensions, mermaid-cli).
"""
import argparse
import sys
import os
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required to run this script.", file=sys.stderr)
    sys.exit(1)


def load_graph(graph_path: Path) -> dict:
    with graph_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_mermaid(graph: dict) -> str:
    lines = ["flowchart TD"]
    # Define nodes
    for node in graph.get("nodes", []):
        node_id = node.get("id")
        kind = node.get("kind")
        label = node_id  # could use description but keep succinct
        # Use different shapes by class definitions
        lines.append(f"{node_id}[\"{label}\"]")
    # Define edges
    for node in graph.get("nodes", []):
        node_id = node.get("id")
        kind = node.get("kind")
        if kind == "activity":
            target = node.get("next")
            if target:
                lines.append(f"{node_id} --> {target}")
        elif kind == "decision":
            for branch in node.get("next", []):
                when = branch.get("when", "cond")
                target = branch.get("node")
                # Use pipe labels for conditions
                lines.append(f"{node_id} --|{when}|--> {target}")
        elif kind == "gate":
            p = node.get("pass")
            f = node.get("fail")
            if p:
                lines.append(f"{node_id} -- pass --> {p}")
            if f:
                lines.append(f"{node_id} -- fail --> {f}")
    # Class definitions for styling
    lines.append("classDef gate fill:#FFF3CD,stroke:#E0A800,stroke-width:2px;")
    lines.append("classDef decision fill:#D1ECF1,stroke:#0C5460,stroke-width:2px;")
    lines.append("classDef activity fill:#E2E3E5,stroke:#6C757D,stroke-width:2px;")
    # Assign classes
    for node in graph.get("nodes", []):
        node_id = node.get("id")
        kind = node.get("kind")
        lines.append(f"class {node_id} {kind};")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render process graph to Mermaid")
    parser.add_argument("--output", type=str, default=None, help="Output file for mermaid diagram")
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    graph_path = repo_root / ".process" / "graph.yaml"
    graph = load_graph(graph_path)
    mermaid = build_mermaid(graph)
    if args.output:
        out_path = Path(args.output)
        out_path.write_text(mermaid, encoding="utf-8")
        print(f"Mermaid diagram written to {out_path}")
    else:
        print(mermaid)
    return 0


if __name__ == "__main__":
    sys.exit(main())