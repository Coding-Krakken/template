package process.recalibration

# Policy for determining when a recalibration is necessary.
# Input should provide `days_since_last_calibration` and `threshold_days`.
# If the number of days since the last calibration exceeds the threshold, the
# policy signals that recalibration is needed.

default recalibration_needed = false

recalibration_needed {
  input.days_since_last_calibration > input.threshold_days
}