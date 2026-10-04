# Git Advanced: Branch & Pull Request

## Overview

This lesson introduces the Git workflow used in professional software development. It covers how to work safely with branches, collaborate using Pull Requests, and keep the `main` branch stable.

## Topics

* Create and switch branches
* Update the local `main` branch
* Push a branch to GitHub
* Create and merge a Pull Request
* Delete completed branches

## Commands

```bash
git branch
git switch -c feat/login
git switch main
git pull origin main
git push --set-upstream origin feat/login
git merge feat/login
git branch -d feat/login
git push origin --delete feat/login
```

## Workflow

```text
main
↓
git pull
↓
Create a branch
↓
Develop
↓
Commit
↓
Push
↓
Pull Request
↓
Review
↓
Merge
↓
Delete the branch
```

## Best Practices

* Never commit directly to `main`.
* Create a separate branch for each feature or bug fix.
* Merge changes through a Pull Request.
* Delete merged branches to keep the repository clean.
