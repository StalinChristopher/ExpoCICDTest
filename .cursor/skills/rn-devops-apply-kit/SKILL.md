---
name: rn-devops-apply-kit
description: >-
  Apply the React Native DevOps GitHub Actions kit from this template into the
  current workspace (another RN repo): rsync .github/.semgrep/.cursor, merge
  .gitignore, bootstrap workflow IDs, generate GITHUB_SECRETS_CHECKLIST.md.
  Use when the user wants one-shot pipeline reuse, CURSOR_RN_DEVOPS_ONE_SHOT,
  or copying RN CI from the template.
---

# RN DevOps kit — apply into this repo

Follow these steps in order. The canonical copy-paste prompt lives at **`CURSOR_RN_DEVOPS_ONE_SHOT_APPLY.txt`** (repository root). Full narrative: **`docs/RN_WORKFLOW_REUSE.md`**.

1. Confirm the workspace root has **`package.json`** (target app, not the template). Ask for **TEMPLATE_ROOT** (absolute path to the template clone) if missing.

2. Run **`rsync`** from **`SETUP_RN_DEVOPS_KIT.md`**: sync `.github/`, `.semgrep/`, `.cursor/` from `TEMPLATE_ROOT` into this repo. Do not overwrite `src/` unless the user explicitly asks.

3. Append lines from **`GITIGNORE_APPEND.txt`** (from `TEMPLATE_ROOT`) that are missing from `.gitignore`.

4. Align **`package.json`** scripts (`lint`, `format:check`, `typecheck`, `test:ci`) if absent — see **`docs/RN_WORKFLOW_REUSE.md`**.

5. Run **`python3 .github/scripts/bootstrap_rn_workflow_ids.py --dry-run`**, then without `--dry-run`. If detection fails (no `ios/`, multiple workspaces), use flags documented in **`docs/RN_WORKFLOW_REUSE.md`**.

6. Run **`python3 .github/scripts/list_workflow_secrets.py --write GITHUB_SECRETS_CHECKLIST.md`**. Remind the user: add secret **values** only in GitHub → Settings → Secrets and variables → Actions.

7. If the user provided a **Git remote URL** and commits exist: configure `origin` and push the current branch per **`git-rn-bootstrap.mdc`** / **`rn-devops-agent-playbook.mdc`**.

Keep **signing / Firebase / store credentials** separate from Git remote setup in the handoff summary.
