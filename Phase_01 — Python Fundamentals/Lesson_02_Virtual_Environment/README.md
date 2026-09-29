# Lesson 02: Virtual Environment & pip

## Objective

By the end of this lesson, you will be able to:
- Create and activate a virtual environment using `venv`.
- Verify that Python and `pip` are using the correct environment.
- Install and manage packages with `pip`.
- Understand the purpose of `requirements.txt` and `requirements-dev.txt`.

## Concepts Covered

- Virtual environments (`venv`) and project isolation
- `pip` package manager and Python Package Index (PyPI)
- Package management with `requirements.txt` and `requirements-dev.txt`
- Creating, activating, and managing virtual environments
- Verifying correct Python interpreter and pip version

## Files

- `README.md` — lesson content and reference (this file)
- `NOTES_VI.md` — personal notes (optional)

---

## Virtual Environment (`venv`)

A virtual environment is an isolated Python environment for a single project. It contains its own Python interpreter and installed packages, preventing dependency conflicts between different projects.

```
Project_A
└── .venv

Project_B
└── .venv

Project_C
└── .venv
```

Each project should have its own virtual environment.

---

## pip & PyPI

`pip` is Python's package installer. It downloads and installs packages from the **Python Package Index (PyPI)** into the active virtual environment.

```
PyPI
   │
   ▼
pip install package
   │
   ▼
Your virtual environment (.venv)
```

---

## `requirements.txt` vs `requirements-dev.txt`

| File | Contains | Purpose |
|------|----------|---------|
| `requirements.txt` | Packages required to run the project | Runtime dependencies |
| `requirements-dev.txt` | Development tools (e.g. `black`, `flake8`, `pytest`) | Development only |

> **Note:** This lesson does not use any third-party packages yet, so these files are **not needed** at this stage.

---

## Commands Reference

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment (Windows)

```bash
.venv\Scripts\activate
```

### Activate the environment (macOS/Linux)

```bash
source .venv/bin/activate
```

### Exit the environment

```bash
deactivate
```

### Verify the current Python interpreter

```bash
python -c "import sys; print(sys.executable)"
```

### Check pip version

```bash
pip --version
```

### List installed packages

```bash
pip list
```

### Install a package

```bash
pip install <package-name>
```

### Install a specific version

```bash
pip install <package-name>==<version>
```

### Export installed packages

```bash
pip freeze > requirements.txt
```

### Install packages from a requirements file

```bash
pip install -r requirements.txt
```

---

## Important Notes

- Never commit the `.venv` directory to Git.
- Add `.venv/` to `.gitignore`.
- Create `requirements.txt` only when the project uses third-party packages.
- Create `requirements-dev.txt` for development tools such as `black`, `flake8`, and `pytest`.
- On Windows, PowerShell may block script execution. This can be fixed by setting the execution policy to `RemoteSigned` for the current user.

---

## Vocabulary

| English | German |
|---------|--------|
| Virtual Environment | Virtuelle Umgebung |
| Package | Paket |
| Package Manager | Paketmanager |
| Dependency | Abhängigkeit |
| PyPI | Python-Paketindex |
| Requirements | Anforderungen |

---

## Key Takeaways

- Each project should have its own virtual environment.
- `venv` isolates project dependencies.
- `pip` installs packages from PyPI.
- Always verify that you are using the correct Python interpreter.
- Never commit `.venv` to Git.
- Use `requirements.txt` to share project dependencies.

---

**Note:** This lesson focuses on theory and setup. No coding exercises are included — the primary focus is understanding virtual environments and package management concepts.