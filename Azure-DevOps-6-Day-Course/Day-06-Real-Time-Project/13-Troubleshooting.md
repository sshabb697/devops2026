# 13 - Troubleshooting

## Overview

Pipelines fail — that's normal. The skill is diagnosing them quickly. This lesson catalogs the most common Azure DevOps issues and how to fix them, plus a general troubleshooting method.

## A General Method

1. **Read the error** — open the failed step's log; the real cause is usually near the first red line.
2. **Reproduce locally** — run the failing command (`npm ci`, `dotnet build`) on your machine.
3. **Isolate** — re-run with `system.debug = true` for verbose logs.
4. **Check recent changes** — what changed since the last green run (code, YAML, variables, agent)?
5. **Fix, commit, re-run.**

## Common Issues & Fixes

### 1. "No hosted parallelism has been purchased or granted"
- **Cause:** New orgs may need to request the free Microsoft-hosted grant.
- **Fix:** Request the free parallelism grant (a form linked in the error), or use a **self-hosted** agent, or purchase parallel jobs.

### 2. Pipeline doesn't trigger on push
- **Cause:** `trigger` branch filter doesn't match; or YAML on the wrong branch; or triggers overridden in UI settings.
- **Fix:** Verify the `trigger:` section includes your branch; check **Pipeline → Settings → Triggers**.

### 3. Build validation blocks a PR forever
- **Cause:** Required build failing, or the validation pipeline can't run.
- **Fix:** Open the build, fix the failure; ensure the pipeline has access to needed resources.

### 4. "Tests failed" but pass locally
- **Cause:** Environment differences (Node/SDK version, env vars, time zone, missing dependency).
- **Fix:** Pin tool versions (`NodeTool@0`, `UseDotNet@2`); ensure `npm ci` (not `npm install`); set required env vars.

### 5. Artifact not found in deploy stage
- **Cause:** Build didn't publish, or names don't match, or stage `dependsOn` missing.
- **Fix:** Confirm `PublishPipelineArtifact@1` ran; match `artifact` names; ensure `dependsOn: Build`.

### 6. Permission / authorization errors
- **Cause:** Pipeline not authorized to use a resource (service connection, variable group, environment, agent pool).
- **Fix:** Authorize on first use, or grant **pipeline permissions** on the resource.

### 7. Secret is empty in a script
- **Cause:** Secret variables aren't auto-mapped into scripts.
- **Fix:** Map via `env:`:
  ```yaml
  - script: ./deploy.sh
    env:
      API_KEY: $(apiKey)
  ```

### 8. YAML syntax / indentation errors
- **Cause:** Tabs, misaligned indentation, wrong nesting.
- **Fix:** Use **spaces**; validate in the YAML editor (**Validate**); check the schema.

### 9. Deployment stuck "waiting"
- **Cause:** Pending **approval** or unmet **check** (branch control, business hours).
- **Fix:** Approve the run; ensure you're deploying from an allowed branch / within allowed hours.

### 10. Self-hosted agent offline
- **Cause:** Agent service stopped, machine down, or token expired.
- **Fix:** Restart the agent service (`svc.sh start`), check connectivity, re-configure with a fresh PAT.

### 11. Service connection authentication failed
- **Cause:** Expired secret/service principal, wrong scope, or revoked permissions.
- **Fix:** Re-create/verify the connection; prefer **workload identity federation** to avoid expiring secrets.

### 12. Merge conflicts blocking a PR
- **Cause:** Target branch advanced and overlaps your changes.
- **Fix:** Merge `main` into your branch locally, resolve, push (Day 2, lesson 09).

## Tools That Help

- **Verbose logs:** `system.debug = true`.
- **Download logs** for full output.
- **Re-run failed jobs** (rather than the whole pipeline).
- **Pipeline → Analytics** to spot flaky/slow steps.
- **Validate** button in the YAML editor.

## Verification

- [ ] You can locate and read a failed step's log.
- [ ] You know how to enable verbose logging.
- [ ] You can map the symptom to a likely cause above.

## Summary

- Troubleshoot methodically: read the error, reproduce, isolate, check changes, fix.
- Know the common failures: parallelism, triggers, artifacts, permissions, secrets, YAML, stuck approvals, agents, connections.
- Use verbose logs, re-runs, and the YAML validator.

➡️ Next: [14 - Best Practices](./14-Best-Practices.md)
