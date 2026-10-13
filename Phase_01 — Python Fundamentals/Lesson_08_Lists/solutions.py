"""
Lesson 08: Lists - Solutions
Topics: comparison operators, if / elif / else,
        logical operators (and, or, not), ternary (conditional) expression
Author: Tran Ngoc
"""

# --- Exercise 1: Positive, Negative, or Zero ---
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# --- Exercise 2: Even or Odd (Ternary) ---
integer = int(input("Enter an integer: "))

# A single ternary expression chooses between the two strings
parity = "even" if integer % 2 == 0 else "odd"
print(f"{integer} is {parity}")


# --- Exercise 3: Leap Year ---
year = int(input("Enter a year: "))

# Divisible by 4 and not by 100, or divisible by 400
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# --- Exercise 4: Grade Classifier ---
score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a number between 0 and 100.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# --- Exercise 5: Largest of Three Numbers ---
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

# Compare each number with the other two, without using max()
if first >= second and first >= third:
    largest = first
elif second >= first and second >= third:
    largest = second
else:
    largest = third

print(f"The largest number is {largest}")


# --- Exercise 6: Triangle Checker ---
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))

if side_a <= 0 or side_b <= 0 or side_c <= 0:
    print("Invalid side length.")
elif (
    side_a + side_b <= side_c
    or side_a + side_c <= side_b
    or side_b + side_c <= side_a
):
    # The sum of any two sides must be greater than the third side
    print("Not a valid triangle")
elif side_a == side_b == side_c:
    print("Equilateral triangle")
elif side_a == side_b or side_b == side_c or side_a == side_c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


# --- Exercise 7: Ticket Price ---
ticket_age = int(input("Enter your age: "))
is_student = input("Are you a student? (y/n): ") == "y"

if ticket_age < 0:
    print("Invalid age.")
else:
    if ticket_age < 5:
        price = 0
    elif ticket_age < 18:
        price = 50
    elif ticket_age < 65:
        # Student discount only applies to ages 18-64
        price = 80 if is_student else 100
    else:
        price = 70

    print(f"Ticket price: {price}")
