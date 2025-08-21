---
id: run-XXXX
type: experiment
feature_flag: feature_example
audience: 5%  # percentage of users exposed to the experiment
metrics:
  lift_primary: ab.example_feature.revenue_delta
  guardrail: error_budget.example_service.burn_rate
result: pending  # pending | pass | fail
---

## Experiment Design

Describe the hypothesis you are testing, the key metrics you will monitor,
and the expected outcomes.  Include details on audience segmentation,
duration, and rollout plan.

## Results

Summarize the outcomes once the experiment has completed.  Include statistical
significance, observed lift or degradation, and any operational impacts.  Decide
whether to proceed to full release, iterate, or abandon the change based on
these results.