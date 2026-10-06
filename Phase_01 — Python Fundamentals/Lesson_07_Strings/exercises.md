# Lesson 07: Strings — Practice Exercises

**Topics:** f-strings, string slicing, string methods, string comparison

**Author:** Tran Ngoc

---

## Exercise 1: f-strings

Declare 3 variables: `product` (product name), `price` (float), and `quantity` (int). Use an f-string to print a sentence such as:

```
You bought 3 x Laptop for a total of: 1500.00 EUR
```

The total must be calculated directly inside `{}` (no separate total variable), formatted to 2 decimal places.

---

## Exercise 2: Slicing

Given `code = "PY-2026-FIAE-0012"`, use slicing only (no `split()`) to extract:

1. The language code (`"PY"`)
2. The year (`"2026"`)
3. The last 4 characters
4. The entire string reversed

---

## Exercise 3: String Methods

Given `raw = "   Rohde   &   SCHWARZ   "`, write code that:

1. Removes the extra whitespace at the start/end with `strip()`
2. Converts the whole string to lowercase with `lower()`
3. Replaces `"&"` with `"and"` using `replace()`
4. Splits the result into a list of words with `split()`, and prints that list

---

## Exercise 4: String Comparison

Simulate comparing two usernames (no `input()` needed):

```python
username_input = "Ngoc"
username_stored = "ngoc"
```

Print `True`/`False` for:

1. A direct comparison with `==` (no normalization)
2. A comparison after normalizing both to lowercase

---

## Exercise 5: Combined Practice (Advanced)

Given `log_line = "  2026-08-12 | ERROR | Connection Failed  "`, write code that:

1. Strips the extra whitespace
2. Splits the string into 3 parts using `"|"`, stripping each part
3. Prints the result in a new f-string format (reordering the extracted variables), e.g.:

```
[ERROR] 2026-08-12: Connection Failed
```