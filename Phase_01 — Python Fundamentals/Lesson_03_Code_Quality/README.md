# Lesson 03: Code Quality Tools (Black & Flake8)

## Objective

By the end of this lesson, you will be able to:
- Install and configure **Black** (Python code formatter).
- Install and configure **Flake8** (Python linter).
- Understand the difference between a formatter and a linter.
- Configure `.editorconfig` for consistent formatting.
- Enable **Format on Save** in VS Code.
- Manage development dependencies with `requirements-dev.txt`.

## Concepts Covered

- Code formatters (Black) and code linters (Flake8)
- PEP 8 style guidelines
- Project configuration files (`.editorconfig`, `.flake8`)
- Development dependencies vs production dependencies
- Automated code quality checks in professional workflows

## Files

- `README.md` — lesson content and reference (this file)
- `.editorconfig` — editor configuration for consistent formatting
- `.flake8` — Flake8 configuration
- `requirements-dev.txt` — development dependencies
- `.gitignore` — Git ignore rules
- `NOTES_VI.md` — personal notes (optional)

---

## Formatter vs Linter

| Aspect | Black | Flake8 |
|--------|-------|--------|
| **Type** | Formatter | Linter |
| **Action** | Auto-fixes code style | Reports issues only |
| **What it fixes** | Spacing, indentation, line length | Unused imports, undefined variables, style violations |
| **Run order** | Run first | Run after Black |

---

## Understanding Black

**Black** is an opinionated Python code formatter that automatically reformats code to comply with PEP 8 style guidelines.

### Key Features:
- Automatic code formatting
- Removes manual style decisions
- Enforces consistent style across a project
- Integrates with editors and CI/CD pipelines

### Common Changes Black Makes:
- Normalizes quotes (single to double)
- Fixes spacing around operators
- Adjusts line length to 88 characters (default)
- Reformats multi-line strings

---

## Understanding Flake8

**Flake8** is a Python linter that checks code for style issues and logical errors that Black cannot fix.

### What Flake8 Detects:
- Unused imports (`F401`)
- Undefined variables (`F821`)
- Whitespace issues (`E201`, `E202`)
- Line too long (`E501`)
- Naming convention violations

### Important Note:
Flake8 does **not** fix issues automatically — it only reports them. You must fix them manually.

---

## Project Structure

```
project/
├── .venv/
├── .editorconfig
├── .flake8
├── .gitignore
├── main.py
├── README.md
└── requirements-dev.txt
```

---

## Tools & Environment

- **Python:** 3.11+
- **Editor:** VS Code
- **Formatter:** Black
- **Linter:** Flake8

---

## Editor Configuration

### `.editorconfig`

Enforces consistent formatting rules (indentation, line endings, charset) across different editors and IDEs.

**Example `.editorconfig`:**
```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true

[*.py]
indent_style = space
indent_size = 4
```

### `.flake8`
Configures Flake8 behavior and ensures it syncs with Black.

**Example `.flake8`:**
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .venv,__pycache__
```

---

## Commands Reference

### Install development dependencies

```bash
pip install -r requirements-dev.txt
```

### Format code with Black

```bash
black .
```

### Check code quality with Flake8

```bash
flake8 .
```

### Format a specific file

```bash
black filename.py
```

### Check a specific file

```bash
flake8 filename.py
```

---

## VS Code Setup

### Enable Format on Save:

1. Open VS Code settings (`Ctrl+,` or `Cmd+,`)
2. Search for "format on save"
3. Enable **Editor: Format On Save**
4. Set default formatter to Black

### Install Black Extension (optional):
- Search for "Black Formatter" in VS Code Extensions
- Install the official extension

---

## `requirements-dev.txt`

Development dependencies are separate from production dependencies.

**Example `requirements-dev.txt`:**
```
black==23.12.1
flake8==6.1.0
```

### Why separate?
- Production environment only needs production dependencies
- Development environment needs both production + development tools
- Reduces deployment size and complexity

---

## Workflow

1. **Write code** in `main.py`
2. **Format** with Black: `black .`
3. **Check** with Flake8: `flake8 .`
4. **Fix** any Flake8 errors manually
5. **Commit** when all checks pass

---

## Important Notes

- Black and Flake8 are **optional** but highly recommended in professional workflows
- Many German companies use these tools as part of code quality standards
- Always run Black before Flake8
- Add `.venv/` to `.gitignore` to prevent committing the virtual environment
- Never commit development tools (`.venv/`, `__pycache__/`) to Git

---

## Vocabulary

| English | German |
|---------|--------|
| Code formatter | Code-Formatter |
| Linter | Linter |
| Code quality | Code-Qualität |
| Style guide | Stilrichtlinie |
| Configuration | Konfiguration |

---

## Key Takeaways

- **Black** formats code automatically; **Flake8** reports issues only
- Run Black first, then Flake8
- Use `.editorconfig` for consistent editor behavior
- Separate development dependencies in `requirements-dev.txt`
- Code quality tools are industry standard in professional environments
- Automating code formatting saves time and prevents style debates

---

**Note:** Refer to the project files (`.editorconfig`, `.flake8`, `requirements-dev.txt`) for configuration examples.