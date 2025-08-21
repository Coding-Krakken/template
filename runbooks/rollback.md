# Rollback Procedures

When a deployment causes a serious regression or incident, perform a rollback to
restore the last known good state.  Follow these steps to ensure a safe and
effective rollback.

## Prerequisites

* Identify the deployment or feature flag that introduced the issue.
* Ensure that the previous version is healthy and available for rollback.
* Verify that database migrations are reversible or safe to run backwards.

## Rollback Steps

1. **Communicate**: Announce the intent to roll back in the incident channel.  Include the reason and expected timeline.
2. **Pause New Deployments**: Freeze the deployment pipeline to prevent additional changes during the rollback.
3. **Disable Feature Flags**: If the issue is behind a flag, disable the flag for all users.  Monitor to confirm resolution.
4. **Redeploy Previous Version**: Use your deployment tool to deploy the last good build.  Confirm that the correct version is running.
5. **Database Rollback**: If necessary, execute rollback scripts or restore backups.  Validate data integrity post‑rollback.
6. **Verify and Monitor**: Check logs, metrics, and user reports to ensure the issue is resolved.  Keep heightened monitoring for at least one hour.
7. **Document**: Update the incident timeline and prepare a postmortem.  Identify root causes and preventive measures.

## Post‑Rollback Considerations

* Investigate the underlying cause of the failure and update test suites to catch similar issues in the future.
* Schedule a follow‑up deployment once the root cause is fixed and verified.