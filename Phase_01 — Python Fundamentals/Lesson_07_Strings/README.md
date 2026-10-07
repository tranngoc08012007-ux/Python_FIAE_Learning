# Lesson 07 — Strings

## Topics Covered

- f-strings (formatted string literals)
- String slicing (`start:stop:step`, negative indices, reversing)
- Common string methods: `strip()`, `split()`, `join()`, `upper()`, `lower()`, `replace()`
- String comparison

## Concepts

### 1. f-strings

Embed variables and expressions directly inside a string using `{}`, with an `f` prefix. f-strings are cleaner and more readable than manual string concatenation with `+`.

```python
print(f"Hello {name}, you are {age} years old")
print(f"Price: {price:.2f} EUR")
```

### 2. String Slicing

Extract part of a string using `string[start:stop:step]`.

- `start` is inclusive.
- `stop` is exclusive.
- Negative indices count from the end.
- A negative step can be used to reverse a string.

```python
text[0:5]    # first 5 characters
text[-4:]    # last 4 characters
text[::-1]   # reversed
```

### 3. Common String Methods

- `strip()` — removes leading and trailing whitespace
- `split(sep)` — splits a string into a list of parts
- `join(iterable)` — joins iterable elements into a single string using a separator
- `upper()` / `lower()` — converts a string to uppercase or lowercase
- `replace(old, new)` — replaces occurrences of a substring

**Example:**

```python
location = "  berlin, germany  "
cleaned = location.strip()
parts = cleaned.split(",")
country = parts[1].strip().upper()
```

### 4. String Comparison

Strings are compared lexicographically based on their Unicode values. Comparisons are case-sensitive.

```python
"Apple" < "apple"   # True
"apple" == "Apple"  # False
```

When comparing user input, normalize the strings first if the comparison should be case-insensitive:

```python
"apple".lower() == "Apple".lower()  # True
```

## Why It Matters

String handling is used constantly in real applications. It is essential for:

- Cleaning and validating user input
- Parsing structured data such as IDs, logs, and CSV data
- Formatting output for users
- Normalizing text before comparison or storage

Understanding strings is therefore an important foundation for application development.

## Exercises

- Created a formatted greeting using f-strings with an inline calculation.
- Used string slicing, without `split()`, to extract a country code, year, and ID number from a structured string.
- Cleaned and parsed a raw location string using `strip()`, `split()`, and `upper()`.

## Files

- `main.py` — examples and completed exercises covering all four topics above.
