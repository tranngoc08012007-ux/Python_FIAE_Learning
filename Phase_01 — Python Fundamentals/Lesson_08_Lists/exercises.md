# Lesson 08: Lists — Exercises

Write each solution in `solutions.py`. Use `input()` to read data from the user, and remember to cast the input to the correct type.

## Exercise 7: Ticket Price

Ask the user to enter their age and whether they are a student (`y` or `n`). Calculate the ticket price:

| Age | Price |
|-----|-------|
| 0–4 | 0 |
| 5–17 | 50 |
| 18–64 | 100 |
| 65 and above | 70 |

**Student discount:** a student aged 18 to 64 pays 80 instead of 100.

If the age is negative, print `Invalid age.`

**Examples:**
```
Enter your age: 20
Are you a student? (y/n): y
Ticket price: 80
```
```
Enter your age: 3
Are you a student? (y/n): n
Ticket price: 0
```
