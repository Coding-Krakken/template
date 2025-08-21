# Release Steps

Use this runbook to perform a well‑controlled release.  Modify to suit your
deployment tooling and organizational requirements.

## Pre‑Release Checklist

* All gates in `.process/graph.yaml` have been passed and evidence is attached.
* Regression, performance, and security tests are green.
* A release candidate build is available and verified.
* Stakeholders are informed of the release date and contents.
* Rollback plan and feature flags are ready.

## Release Process

1. **Tag and Build**: Create a release tag in version control and build the release artifact.
2. **Canary Deployment**: Deploy the release to a small percentage of traffic (canary).  Monitor metrics and error budgets for a defined period.
3. **Gradual Rollout**: If the canary is stable, gradually increase exposure (e.g. 25%, 50%, 100%).  Monitor at each step.
4. **Full Release**: Roll out to 100% of users once metrics are stable and error budgets are within limits.
5. **Post‑Release Verification**: Execute smoke tests and user experience checks.  Confirm that no major regressions exist.
6. **Communicate**: Announce the successful release to stakeholders, update release notes, and close related tickets.

## Post‑Release Activities

* Monitor metrics and logs closely for 24–48 hours after release.
* Document any deviations from the process and update runbooks accordingly.
* Gather feedback from users and stakeholders to inform the next iteration.