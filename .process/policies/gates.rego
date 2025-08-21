package process.gates

# Example policy for gate evaluation.
# This policy expects an input document with two lists:
#   artifacts_missing: a list of artifact IDs that are required but not found
#   metrics_failing: a list of metric names that do not meet their targets
# The gate is allowed only if both lists are empty.

default allow = false

allow {
  not artifacts_missing[_]
  not metrics_failing[_]
}

artifacts_missing[id] {
  id := input.artifacts_missing[_]
}

metrics_failing[name] {
  name := input.metrics_failing[_]
}