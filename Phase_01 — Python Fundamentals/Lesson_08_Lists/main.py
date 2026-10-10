"""
Lesson 08: Control Flow
Topics: comparison operators, if / elif / else, logical operators (and, or, not),
        ternary (conditional) expression
Author: Tran Ngoc
"""

# --- 1. Comparison Operators ---
# Comparison operators always return a bool (True or False)
a = 10
b = 3

print(f"{a} == {b}: {a == b}")  # Equal to: False
print(f"{a} != {b}: {a != b}")  # Not equal to: True
print(f"{a} > {b}: {a > b}")  # Greater than: True
print(f"{a} < {b}: {a < b}")  # Less than: False
print(f"{a} >= 10: {a >= 10}")  # Greater than or equal to: True
print(f"{b} <= 2: {b <= 2}")  # Less than or equal to: False

# Python supports chained comparisons, just like in math
age = 18
print(f"18 <= {age} < 65: {18 <= age < 65}")  # True

# Remember: '=' assigns a value, '==' compares two values


# --- 2. if / elif / else ---
# Python checks the branches from top to bottom
# and runs ONLY the first branch whose condition is True
score = 75

if score >= 90:
    grade = "A"  # Runs only if score >= 90
elif score >= 80:
    grade = "B"  # Runs only if score is 80-89
elif score >= 70:
    grade = "C"  # Runs only if score is 70-79
else:
    grade = "F"  # Runs if none of the conditions above is True

print(f"Score: {score}, Grade: {grade}")  # Output: Score: 75, Grade: C

# Do not forget the colon ':' and the 4-space indentation
# Nested if: an if statement placed inside another if statement
has_ticket = True
if has_ticket:
    if age >= 18:
        print("Entry allowed: adult with ticket.")
    else:
        print("Entry allowed only with a guardian.")
else:
    print("Entry denied: no ticket.")


# --- 3. Logical Operators (and, or, not) ---
# and: True only if BOTH conditions are True
# or: True if AT LEAST ONE condition is True
# not: reverses the boolean value
has_license = True
is_weekend = False
is_holiday = True

print(f"Can rent a car: {age >= 18 and has_license}")  # True
print(f"Day off: {is_weekend or is_holiday}")  # True
print(f"Not weekend: {not is_weekend}")  # True

# Precedence: not -> and -> or (use parentheses to make the intent clear)
print(f"True or False and False: {True or False and False}")  # True
print(f"(True or False) and False: {(True or False) and False}")  # False

# Short-circuit: in 'A and B', if A is False, B is never evaluated
divisor = 0
if divisor != 0 and 10 / divisor > 1:
    print("Result is greater than 1.")
else:
    print("Safe: 10 / divisor was never evaluated.")  # No ZeroDivisionError

# Truthy and falsy: 0, 0.0, "", [], None are treated as False in a condition
shopping_list = []
if shopping_list:
    print("The list has items.")
else:
    print("The list is empty.")  # Runs, because [] is falsy


# --- 4. Ternary (Conditional) Expression ---
# Syntax: value_if_true if condition else value_if_false

# Long version (4 lines)
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Short version (1 line), same result
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")  # Output: Status: adult

# Ternary inside an f-string
number = 7
print(f"{number} is {'even' if number % 2 == 0 else 'odd'}")  # Output: 7 is odd

# Use a ternary only for simple choices between two values
# For more complex logic, use a normal if / elif / else


# --- 5. Input and Conditions ---
# Remember: input() always returns a string, so cast it before comparing numbers
user_score = int(input("Enter your score (0-100): "))

if user_score < 0 or user_score > 100:
    print("Invalid score. Please enter a number between 0 and 100.")
elif user_score >= 50:
    print("Result: Passed")
else:
    print("Result: Failed")

# Combine the ternary with input for a quick check
parity = "even" if user_score % 2 == 0 else "odd"
print(f"Your score is an {parity} number.")


# --- 6. Final Formatting (f-string) ---
print(f"My name is Ngoc, I am {age} years old, and my status is: {status}.")
