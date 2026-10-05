"""
Lesson 06: Variables & Data Types - Practice Exercises
Solutions

Topics: int, float, str, bool, None, type(), arithmetic operators,
        type casting, advanced print() (sep, end), f-string
"""

# ============================================================
# EXERCISE 1: Personal Information


name = "Ngoc"              # str
age = 18                   # int
height = 1.75              # float
graduated = False          # bool
note = None                # NoneType

print("Data type of each variable:")
print(type(name))
print(type(age))
print(type(height))
print(type(graduated))
print(type(note))

print("-" * 40)

print(f"Name: {name} | Age: {age} | Height: {height}m | Graduated: {graduated} | Note: {note}")


# ============================================================
# EXERCISE 2: Basic Arithmetic Operations
# ============================================================

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(
    f"{num1} + {num2} = {num1 + num2}",
    f"{num1} - {num2} = {num1 - num2}",
    f"{num1} * {num2} = {num1 * num2}",
    f"{num1} / {num2} = {num1 / num2}",
    f"Floor: {int(num1) // int(num2)}",
    f"Remainder: {int(num1) % int(num2)}",
    sep=" | "
)


# ============================================================
# EXERCISE 3: Purchase Invoice
# ============================================================

product_name = input("Enter product name: ")
unit_price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))

subtotal = unit_price * quantity
tax = subtotal * 0.1
grand_total = subtotal + tax

print("===== INVOICE =====")
print(f"Product: {product_name}")
print(f"Unit price: {unit_price} VND")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal} VND")
print(f"Tax (10%): {tax} VND")
print(f"Grand total: {grand_total} VND")
print("====================")

print("\nData type of grand_total:", type(grand_total))
print(
    "Explanation: grand_total is a float because it is the result of "
    "adding subtotal (float) and tax (float). In Python, any arithmetic "
    "operation involving at least one float always returns a float."
)