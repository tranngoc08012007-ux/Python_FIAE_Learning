# Lesson 01: Environment Setup & Hello World

## Objective

By the end of this lesson, you will be able to:
- Run a Python program.
- Use `print()` to display output.
- Write comments in Python.
- Create and use variables.
- Update variable values.
- Follow the `snake_case` naming convention.

## Concepts Covered

- `print()` function for displaying output
- Comments for code documentation
- Variables and variable assignment
- Variable naming conventions (`snake_case`)
- Basic data types (strings, integers)

## Files

- `main.py` — core implementation with examples
- `exercises.md` — practice problems
- `solutions.py` — coding solutions for exercises
- `NOTES_VI.md` — personal notes (optional)

## How to Run

```bash
python main.py
```

---

## Key Concepts

### `print()`

Displays output on the screen.

```python
print("Hello, World!")
print(2 + 3)
```

### Comments

Comments are ignored by Python and help explain the code.

```python
# This is a comment
```

### Variables

Variables store data that can be reused later.

```python
name = "Ngoc"
birth_year = 2007
current_year = 2026

age = current_year - birth_year
```

Variables can also be updated.

```python
age = age + 1
```

### Naming Convention

Use **snake_case** for variable names.

✅ Good

```python
birth_year
current_year
user_name
```

❌ Avoid

```python
birthYear
BirthYear
birth year
```

## Common Mistakes

- Forgetting quotation marks for strings.
- Using spaces in variable names.
- Hardcoding values instead of using variables.

## Vocabulary

| English | German |
|---------|--------|
| Variable | Variable |
| Comment | Kommentar |
| Function | Funktion |
| Output | Ausgabe |
| String | Zeichenkette |

## Self-Check Questions

- What does `print()` do?
- What is a variable?
- Why do we use comments?
- Why should we avoid hardcoded values?
- What is `snake_case`?

---

**Note:** Refer to `exercises.md` for practice problems. Try solving them independently before checking `solutions.py`.