# Lesson 06: Variables & Data Types - Practice Exercises

**Topics:** int, float, str, bool, None, type(), arithmetic operators, type casting, advanced print() (sep, end), f-string

---

## EXERCISE 1: Personal Information

1. Declare 5 variables with 5 different data types (str, int, float, bool, None) describing a person
2. Use `type()` to print the data type of each variable
3. Print the person's info using an f-string in this format:
   ```
   Name: Ngoc | Age: 18 | Height: 1.75m | Graduated: False | Note: None
   ```

---

## EXERCISE 2: Simple Calculator

1. Use `input()` to get 2 numbers from the user (cast to float right when receiving them)
2. Calculate and print the result of all 4 basic operators: `+`, `-`, `*`, `/`
3. Add floor division `//` and modulus `%` (cast to int first)
4. Use `sep=" | "` to print all results on the same line

---

## EXERCISE 3: Purchase Invoice

1. Use `input()` to get: product name (str), unit price (float), and quantity (int)
2. Calculate: `subtotal = unit_price * quantity`
3. Calculate 10% tax: `tax = subtotal * 0.1`
4. Calculate the grand total: `grand_total = subtotal + tax`
5. Print the invoice in a formatted table
6. Use `type()` to print the data type of `grand_total`, and explain why it has that type