"""
Lesson 09: Control Flow
Topics: if / elif / else, logical operators (and, or, not),
        comparison operators, ternary (conditional) expression
Author: Tran Ngoc
"""

# --- 1. if / elif / else ---
# if: runs a block of code only when the condition is True
temperature = 32
if temperature > 30:
    print("It is hot today.")  # Runs, because 32 > 30

# if / else: choose between two blocks
balance = 50
price = 80
if balance >= price:
    print("Payment successful.")
else:
    print("Not enough money.")  # Runs, because 50 < 80

# if / elif / else: choose between many blocks
# Python checks from top to bottom and runs ONLY the first True branch
light = "yellow"
if light == "green":
    print("Go.")
elif light == "yellow":
    print("Slow down.")  # Runs, because light == "yellow"
elif light == "red":
    print("Stop.")
else:
    print("Invalid light color.")

# Do not forget the colon ':' and the 4-space indentation
# Nested if: an if statement placed inside another if statement
is_logged_in = True
is_admin = False
if is_logged_in:
    if is_admin:
        print("Welcome, admin.")
    else:
        print("Welcome, user.")  # Runs
else:
    print("Please log in first.")

# Combine with input(): remember that input() always returns a string
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")


# --- 2. Logical Operators (and, or, not) ---
# and: True only if BOTH sides are True
# or: True if AT LEAST ONE side is True
# not: reverses the boolean value
age = 20
has_id = True
print(f"Can enter the club: {age >= 18 and has_id}")  # True

day = "Sat"
print(f"Is weekend: {day == 'Sat' or day == 'Sun'}")  # True

is_raining = False
print(f"Can go outside: {not is_raining}")  # True

print(f"True and False: {True and False}")  # False
print(f"True or False: {True or False}")  # True
print(f"not True: {not True}")  # False

# Precedence: comparison -> not -> and -> or
# Use parentheses to make your intention clear
print(f"True or False and False: {True or False and False}")  # True
print(f"(True or False) and False: {(True or False) and False}")  # False

# Common mistake: 'x == 1 or 2' is ALWAYS True, because 2 is truthy
x = 5
print(f"Wrong: {bool(x == 1 or 2)}")  # True
print(f"Correct: {x == 1 or x == 2}")  # False

# Short-circuit: in 'A and B', if A is False, B is never evaluated
name = ""
if name and name[0] == "N":  # name[0] would raise IndexError on ""
    print("The name starts with N.")
else:
    print("The name is empty or does not start with N.")  # Runs, no error

# Falsy values: False, None, 0, 0.0, "" (empty string), [] (empty list)
# Every other value is truthy


# --- 3. Comparison Operators ---
# Comparison operators always return a bool (True or False)
x = 7
y = 12

print(f"{x} == {y}: {x == y}")  # Equal to: False
print(f"{x} != {y}: {x != y}")  # Not equal to: True
print(f"{x} > {y}: {x > y}")  # Greater than: False
print(f"{x} < {y}: {x < y}")  # Less than: True
print(f"{x} >= 7: {x >= 7}")  # Greater than or equal to: True
print(f"{y} <= 10: {y <= 10}")  # Less than or equal to: False

# Remember: '=' assigns a value, '==' compares two values
# Chained comparison, just like in math
month = 10
print(f"Valid month: {1 <= month <= 12}")  # True

# int and float can be equal, but str and int cannot
print(f"5 == 5.0: {5 == 5.0}")  # True
print(f"'5' == 5: {'5' == 5}")  # False

# Strings are case-sensitive and compared character by character
print(f"'apple' == 'Apple': {'apple' == 'Apple'}")  # False
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # True

# Floats: avoid '==' because of rounding errors
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False
print(f"With round(): {round(0.1 + 0.2, 2) == 0.3}")  # True


# --- 4. Ternary (Conditional) Expression ---
# Syntax: value_if_true if condition else value_if_false
score = 72
result = "Passed" if score >= 50 else "Failed"
print(f"Score {score}: {result}")  # Output: Score 72: Passed

# Same logic written with a normal if / else (4 lines)
if score >= 50:
    result = "Passed"
else:
    result = "Failed"

# Ternary inside an f-string
count = 1
print(f"You have {count} {'item' if count == 1 else 'items'}.")  # 1 item

# Default value when a string is empty (an empty string is falsy)
nickname = ""
display_name = nickname if nickname else "Guest"
print(f"Hello, {display_name}!")  # Output: Hello, Guest!

# Nested ternary works, but it is hard to read
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(f"Grade: {grade}")  # Output: Grade: C

# Rule of thumb: use a ternary for SIMPLE choices between two values
# For more complex logic, use a normal if / elif / else


# --- 5. Putting It Together: Discount Calculator ---
shop_price = float(input("Enter the price: "))
is_member = input("Are you a member? (y/n): ") == "y"

if shop_price <= 0:
    print("Invalid price.")
else:
    if is_member and shop_price >= 100:
        discount = 0.2  # Members get 20% off on orders from 100
    elif is_member:
        discount = 0.1  # Members get 10% off on smaller orders
    elif shop_price >= 200:
        discount = 0.05  # Non-members get 5% off on orders from 200
    else:
        discount = 0

    final_price = shop_price * (1 - discount)
    print(f"Discount: {discount * 100:.0f}%")
    print(f"Final price: {final_price:.2f}")


# --- 6. Final Formatting (f-string) ---
age_group = "an adult" if age >= 18 else "a minor"
print(f"My name is Ngoc, I am {age} years old, and I am {age_group}.")
