# Contributing

Thank you for contributing to this repository. This project is centred on documentation, repository maintenance, and GitHub Actions workflows, so contributions should be focused, well explained, and easy to review.

## Contribution workflow

1. **Create a branch**
   - Branch from `master`.
   - Use a short, descriptive branch name that reflects the change you are making.

2. **Make focused changes**
   - Keep each pull request limited to a single improvement or closely related set of changes.
   - Update related documentation when changing repository workflows, prompts, or reporting behaviour.
   - Avoid committing temporary files, local experiment output, or unrelated formatting changes.

3. **Validate your work**
   - Check that key documentation files still exist and are up to date, especially `README.md`, `CONTRIBUTING.md`, and files under `docs/`.
   - If you change a workflow in `.github/workflows/`, review the trigger conditions, permissions, and any generated files affected by the change.
   - If your update affects automation behaviour, include a short note in the pull request describing how you verified it.

4. **Commit clearly**
   - Use a concise commit message that explains the outcome of the change.
   - Group related edits together so the commit history remains easy to follow.

5. **Submit a pull request**
   - Summarise what changed, why it changed, and any validation you performed.
   - Link related issues, workflow runs, or supporting documentation when relevant.

6. **Ensure workflows pass**
   - Review GitHub Actions results before requesting approval.
   - Address review comments with small follow-up commits that keep the scope of the pull request clear.
