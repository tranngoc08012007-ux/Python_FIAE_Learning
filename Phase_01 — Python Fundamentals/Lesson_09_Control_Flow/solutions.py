"""
Lesson 09: Control Flow - Solutions
Topics: if / elif / else, logical operators (and, or, not),
        comparison operators, ternary (conditional) expression
Author: Tran Ngoc
"""

# --- Exercise 1: Age Category ---
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age <= 12:
    print("Category: Child")
elif age <= 17:
    print("Category: Teenager")
elif age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior")


# --- Exercise 2: Login Check ---
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login successful.")
elif username == "admin":
    print("Wrong password.")  # Username is correct, so the password is wrong
else:
    print("Unknown user.")


# --- Exercise 3: Store Open or Closed ---
hour = int(input("Enter the hour (0-23): "))
is_holiday = input("Is today a holiday? (y/n): ") == "y"

if hour < 0 or hour > 23:
    print("Invalid hour.")
elif 8 <= hour < 20 and not is_holiday:
    # Chained comparison: 8:00 to 19:59, and today must not be a holiday
    print("The store is open.")
else:
    print("The store is closed.")


# --- Exercise 4: Season ---
month = int(input("Enter a month (1-12): "))

if month < 1 or month > 12:
    print("Invalid month.")
elif month == 12 or month <= 2:
    print("Season: Winter")
elif month <= 5:
    print("Season: Spring")
elif month <= 8:
    print("Season: Summer")
else:
    print("Season: Autumn")


# --- Exercise 5: Plural Form ---
item_count = int(input("Enter the number of items: "))

# A single ternary expression chooses between the singular and plural word
word = "item" if item_count == 1 else "items"
print(f"You have {item_count} {word}.")


# --- Exercise 6: Rock, Paper, Scissors ---
first = input("Player 1 (rock/paper/scissors): ")
second = input("Player 2 (rock/paper/scissors): ")

is_first_valid = first == "rock" or first == "paper" or first == "scissors"
is_second_valid = second == "rock" or second == "paper" or second == "scissors"

if not (is_first_valid and is_second_valid):
    print("Invalid choice.")
elif first == second:
    print("Draw.")
elif (
    (first == "rock" and second == "scissors")
    or (first == "scissors" and second == "paper")
    or (first == "paper" and second == "rock")
):
    print("Player 1 wins.")
else:
    print("Player 2 wins.")


# --- Exercise 7: Shipping Fee ---
weight = float(input("Enter the weight (kg): "))
is_express = input("Express delivery? (y/n): ") == "y"

if weight <= 0:
    print("Invalid weight.")
elif weight > 20:
    print("Package too heavy.")
else:
    # Base fee depends on the weight
    if weight <= 1:
        fee = 20
    elif weight <= 5:
        fee = 35
    else:
        fee = 55

    # Express delivery adds a fixed amount
    if is_express:
        fee += 15

    print(f"Shipping fee: {fee}")
