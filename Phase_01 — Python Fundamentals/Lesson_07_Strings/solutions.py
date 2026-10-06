"""
Lesson 07: Strings
Solutions

Author: Tran Ngoc
"""

# ==========================================================
# Exercise 1: f-strings
# ==========================================================
product = "Laptop"
price = 500.0  # price per unit
quantity = 3

print(f"You bought {quantity} x {product} for a total of: {price * quantity:.2f} EUR")


# ==========================================================
# Exercise 2: Slicing
# ==========================================================
code = "PY-2026-FIAE-0012"

language = code[0:2]       # or code[:2]
year = code[3:7]
last_four = code[-4:]
reversed_code = code[::-1]

print(f"1. Language: {language}")
print(f"2. Year: {year}")
print(f"3. Last 4 characters: {last_four}")
print(f"4. Reversed: {reversed_code}")


# ==========================================================
# Exercise 3: String Methods
# ==========================================================
raw = "   Rohde   &   SCHWARZ   "

step1 = raw.strip()
step2 = step1.lower()
step3 = step2.replace("&", "and")
result_list = step3.split()

print("Exercise 3 result:", result_list)


# ==========================================================
# Exercise 4: String Comparison
# ==========================================================
username_input = "Ngoc"
username_stored = "ngoc"

direct_compare = username_input == username_stored
normalized_compare = username_input.lower() == username_stored.lower()

print(f"1. Direct comparison: {direct_compare}")
print(f"2. Normalized comparison: {normalized_compare}")


# ==========================================================
# Exercise 5: Combined Practice (Advanced)
# ==========================================================
log_line = "  2026-08-12 | ERROR | Connection Failed  "

cleaned_log = log_line.strip()
parts = cleaned_log.split("|")
date_str = parts[0].strip()
level_str = parts[1].strip()
message_str = parts[2].strip()

print(f"[{level_str}] {date_str}: {message_str}")