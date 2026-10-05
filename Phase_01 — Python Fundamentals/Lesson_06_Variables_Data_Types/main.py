"""
Lesson 06: Variables & Data Types
Topics: int, float, str, bool, None, type(), arithmetic operators,
        type casting, advanced print() and input()
Author: Tran Ngoc
"""

# --- 1. Variable Declaration & Data Types ---
name = "Ngoc"  # str: represents a string of text
age = 18  # int: represents an integer
height = 1.75  # float: represents a floating-point number
is_graduated = False  # bool: represents a boolean (True or False)
note = None  # NoneType: represents the absence of a value

# Check data types using type()
print(f"Type of 'name': {type(name)}")
print(f"Type of 'age': {type(age)}")
print(f"Type of 'height': {type(height)}")
print(f"Type of 'is_graduated': {type(is_graduated)}")
print(f"Type of 'note': {type(note)}")


# --- 2. Basic Arithmetic Operations ---
total = age + 5  # Addition: 23
division = age / 3  # Division (always returns float): 6.0
floor_division = age // 3  # Integer division (floor): 6
remainder = age % 3  # Modulus (remainder): 0

print(
    f"Total: {total}, Division: {division}, "
    f"Floor division: {floor_division}, Remainder: {remainder}"
)


# --- 3. Input and Type Casting ---
# Remember: input() always returns a string!
user_age = input("Enter your age: ")
print(f"Data type before casting: {type(user_age)}")

# Always cast input if you need to perform calculations
age_int = int(input("Enter your age again to calculate: "))
print(f"Next year you will be {age_int + 1} years old.")


# --- 4. Advanced print() usage ---
# 'sep' defines the character placed between items
print("Python", "FAE", "2026", sep=" - ")  # Output: Python - FAE - 2026

# 'end' replaces the default newline at the end of print()
print("Processing", end="...")
print("Done!")  # Output: Processing...Done!


# --- 5. Final Formatting (f-string) ---
print(f"My name is {name}, and I am {age} years old.")
