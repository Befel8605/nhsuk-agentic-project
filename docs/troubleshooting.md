# Troubleshooting

## Agentic Workflow Failures

### Transient Authentication Errors

**Symptom:**

```
Authentication failed with provider at <inference-provider-url> (HTTP 401).
Check your COPILOT_PROVIDER_API_KEY or COPILOT_PROVIDER_BEARER_TOKEN.
Request failed (transient_auth_error). Retrying...
```

**Cause:**

This error occurs when the Copilot engine experiences a temporary authentication failure with the AI inference provider. This is an infrastructure-level issue and is not caused by misconfiguration in the repository.

**Resolution:**

1. **Re-run the workflow** — Transient errors typically resolve on their own. Navigate to the failed workflow run in GitHub Actions and click "Re-run all jobs".
2. **Check GitHub Status** — Visit [githubstatus.com](https://www.githubstatus.com/) to verify there are no ongoing incidents affecting GitHub Copilot or GitHub Actions.
3. **Verify secrets** — Ensure that `COPILOT_GITHUB_TOKEN` is configured in the repository secrets (Settings > Secrets and variables > Actions). This token is typically managed automatically for Copilot-enabled repositories.

### Engine Timeout

**Symptom:**

The workflow fails with a timeout message after the maximum execution time.

**Resolution:**

Re-run the workflow. If timeouts persist, consider simplifying the workflow prompt or reducing the scope of data the agent needs to process.

## GitHub Actions Workflows

### Repository Maintainer

The `repo-maintainer.yml` workflow runs on:
- Push to `master`
- Pull requests to `master`
- Weekly schedule (Monday 9:00 UTC)
- Manual dispatch

If it fails, check that the workflow has `contents: write` permission and that branch protection rules allow the bot to push.

### Documentation Review

The `documentation.yml` workflow prints warnings in the job logs when key documentation files are missing (for example, "README missing" or "LICENSE missing"); add the indicated files in the repository root.
