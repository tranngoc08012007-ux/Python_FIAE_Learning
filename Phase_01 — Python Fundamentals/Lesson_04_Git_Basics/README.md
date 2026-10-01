# Lesson 04: Git Basics

## Objective

By the end of this lesson, you will be able to:
- Understand what Git is and why version control is essential.
- Explain the three areas of Git: Working Directory, Staging Area, and Repository.
- Use basic Git commands (`git init`, `git add`, `git commit`, `git push`, `git pull`).
- Write clear and meaningful commit messages.
- Manage a `.gitignore` file to exclude unnecessary files from Git.
- Understand the Git workflow and version control best practices.

## Concepts Covered

- Version Control System (VCS) and Git fundamentals
- Three Git areas: Working Directory, Staging Area, Repository
- Git workflow and basic commands
- Commit message conventions
- `.gitignore` file and ignoring files
- Git history and version tracking
- Collaboration with GitHub

---

## What is Git?

Git is a **Version Control System (VCS)** that tracks all changes in a project. Every time you save a "checkpoint" (called a **commit**), Git records:
- Who made the change
- What changed
- When it changed

If code breaks or you need to revert to a previous version, Git can restore it easily.

### Git vs GitHub

| Aspect | Git | GitHub |
|--------|-----|--------|
| **Type** | Version Control System (local) | Cloud hosting platform |
| **Location** | Works on your computer | Cloud-based storage |
| **Purpose** | Track changes and history | Backup, share, collaborate |

---

## Why is Git Important?

- **Industry Standard:** Most software companies use Git for source code management
- **Collaboration:** Multiple developers can work on the same project
- **Safety:** Complete history allows rollback to any previous version
- **Portfolio:** A GitHub with clear commit history helps employers evaluate your learning and work
- **Professional Requirement:** Essential skill for any software developer

---

## How Git Works

### Three Areas of Git

```
Working Directory
        │
     git add
        │
   Staging Area
        │
   git commit
        │
 Git Repository
```

**Simple analogy:**
- **Working Directory** = your desk
- **Staging Area** = a bag preparing to send
- **Repository** = long-term storage

---

## Basic Git Commands

### 1. `git init`

Initialize Git for a project and create a hidden `.git/` folder.

The `.git/` folder contains the entire project history.

```bash
git init
```

> Use only once when starting a project.

---

### 2. `git status`

Check the current status of your project.

Shows which files are new, modified, or staged for commit.

```bash
git status
```

---

### 3. `git add`

Move files to the **Staging Area**.

This marks files to be included in the next commit (does not save history yet).

```bash
git add main.py
git add main.py README.md
git add .
```

> `git add .` stages all changes.

---

### 4. `git commit`

Save a version of the project to Git history.

Always use the `-m` flag with a meaningful message.

```bash
git commit -m "feat: add login interface"
git commit -m "fix: correct password validation"
```

---

### 5. `git log`

View the commit history.

```bash
git log
git log --oneline
```

> `--oneline` shows a compact view with one commit per line.

---

### 6. `git diff`

See exactly which lines of code have changed.

```bash
git diff
git diff --staged
```

**Symbols:**
- `-` line removed
- `+` line added

---

### 7. `git restore`

Restore files to the last committed state (undo uncommitted changes).

```bash
git restore main.py
```

> Only works for changes **not yet committed**.

---

### 8. `git rm`

Delete a file from the project and mark the deletion for commit.

```bash
git rm test.py
git commit -m "chore: remove test file"
```

**To stop tracking a file without deleting it:**

```bash
git rm --cached .env
```

---

### 9. `git clone`

Download a Git repository from GitHub to your computer.

```bash
git clone https://github.com/user/project.git
```

> After cloning, **no need** to run `git init`.

---

### 10. `git push`

Push commits from your computer to GitHub.

```bash
git push origin main
```

---

### 11. `git pull`

Fetch the latest changes from GitHub to your computer.

```bash
git pull origin main
```

---

## `.gitignore` File

The `.gitignore` file tells Git which files and folders to ignore.

### Example `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
.env
.vscode/
*.log
```

### Common entries for Python projects:

| Pattern | Purpose |
|---------|---------|
| `.venv/` | Virtual environment folder |
| `__pycache__/` | Python cache folder |
| `*.pyc` | Compiled Python files |
| `.env` | Environment variables (secrets) |
| `.vscode/` | VS Code settings |
| `*.log` | Log files |

---

## Commit Message Convention

Always write clear, meaningful commit messages using this format:

```
<type>: <subject>
```

### Types:

| Type | Use when |
|------|----------|
| `feat` | Adding a new feature |
| `fix` | Fixing a bug |
| `docs` | Updating documentation |
| `style` | Code formatting only (no logic change) |
| `refactor` | Rewriting code |
| `test` | Adding or modifying tests |
| `chore` | Maintenance tasks |

### Rules:

- Write in English
- Keep it concise
- One commit = one purpose

### Examples:

```
feat: add login page
fix: correct password validation
docs: update lesson 4
style: format code with black
chore: remove unused files
refactor: simplify authentication logic
```

---

## Basic Git Workflow

```
Edit files
    │
git status
    │
git diff
    │
git add
    │
git status
    │
git commit
    │
git log
    │
git push
    │
GitHub
```

---

## Vocabulary

| English | German |
|---------|--------|
| Version Control | Versionskontrolle |
| Repository | Repository |
| Commit | Commit |
| Branch | Verzweigung |
| History | Verlauf |
| Staging Area | Staging-Bereich |

---

## Important Notes

- **Commit frequently:** Small, focused commits are better than large ones
- **Clear messages:** Future you and your teammates will thank you
- **Never commit secrets:** Use `.env` and `.gitignore` for API keys and passwords
- **Always `.gitignore` the `.venv/` folder:** Never commit virtual environments
- **Read `.gitignore` carefully:** Before committing, verify that unnecessary files are ignored

---

## Key Takeaways

- Git tracks changes to code over time
- Three areas: Working Directory → Staging Area → Repository
- `git add` stages files, `git commit` saves history
- `git push` sends commits to GitHub, `git pull` brings them back
- Write meaningful commit messages
- Use `.gitignore` to exclude unnecessary files
- Git is essential for professional software development

---

**Note:** For personal notes or practice examples, use `NOTES_VI.md`.