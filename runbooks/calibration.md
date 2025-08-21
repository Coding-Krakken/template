# Recalibration Guide

This guide describes how to perform periodic recalibration sessions, a
cornerstone of the hybrid workflow.  Recalibration ensures your process
continues to reflect reality as your project evolves.

## When to Recalibrate

* On a **regular cadence** (e.g. quarterly or every sprint cycle).
* After **significant incidents** or customer feedback that reveals hidden
  assumptions or requirements.
* When **metrics drift** outside error budgets or business KPIs miss targets.
* Whenever the team feels the existing process is no longer aligned with
  objectives or constraints.

## Preparation

1. **Collect Data**: Gather recent metrics, postmortems, experiment results,
   and any feedback from customers or stakeholders.
2. **Review the Graph**: Examine `.process/graph.yaml` to identify where in the
   process issues are occurring.  Note any gates that are frequently failing or
   any skipped or unclear steps.
3. **Identify Gaps**: List missing artifacts, unclear responsibilities, or
   outdated assumptions.

## Workshop Agenda

1. **State of the Project**: Summarize progress since the last recalibration.
2. **Metrics Review**: Discuss SLO compliance, error budgets, velocity, and
   business KPIs.
3. **Lessons Learned**: Share learnings from recent incidents and experiments.
4. **Gap Analysis**: Identify discrepancies between the documented process and
   actual practice.  Decide whether to adjust the process or enforce existing
   gates more strictly.
5. **Action Items**: Define concrete changes to the process graph, artifacts,
   requirements, or policies.  Assign owners and deadlines.

## Follow‑Up

* Update `graph.yaml`, requirements, and runbooks to reflect decisions.
* Track action items to completion.  Monitor the impact of changes in
  subsequent cycles.