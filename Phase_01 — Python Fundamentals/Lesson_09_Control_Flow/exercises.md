# Lesson 09: Control Flow — Exercises

Write each solution in `solutions.py`. Use `input()` to read data from the user, and remember to cast the input to the correct type.

## Exercise 1: Age Category

Ask the user to enter their age. Print the category:

| Age | Category |
|-----|----------|
| 0–12 | Child |
| 13–17 | Teenager |
| 18–59 | Adult |
| 60 and above | Senior |

If the age is negative, print `Invalid age.`

**Examples:**
```
Enter your age: 15
Category: Teenager
```
```
Enter your age: -3
Invalid age.
```

## Exercise 2: Login Check

The correct account is username `admin` and password `python123`. Ask the user to enter a username and a password, then:

- If both are correct, print `Login successful.`
- If only the username is correct, print `Wrong password.`
- Otherwise, print `Unknown user.`

**Requirement:** Use the logical operator `and`.

**Examples:**
```
Enter username: admin
Enter password: python123
Login successful.
```
```
Enter username: admin
Enter password: 1234
Wrong password.
```

## Exercise 3: Store Open or Closed

A store is open from 8:00 to 19:59 every day, except on holidays when it is always closed.

Ask the user to enter the current hour (0–23) and whether today is a holiday (`y` or `n`). Print `The store is open.` or `The store is closed.`

If the hour is not between 0 and 23, print `Invalid hour.`

**Requirement:** Use a chained comparison and the `not` operator.

**Examples:**
```
Enter the hour (0-23): 10
Is today a holiday? (y/n): n
The store is open.
```
```
Enter the hour (0-23): 10
Is today a holiday? (y/n): y
The store is closed.
```

## Exercise 4: Season

Ask the user to enter a month number (1–12). Print the season:

| Months | Season |
|--------|--------|
| 12, 1, 2 | Winter |
| 3, 4, 5 | Spring |
| 6, 7, 8 | Summer |
| 9, 10, 11 | Autumn |

If the month is not between 1 and 12, print `Invalid month.`

**Requirement:** Use the logical operator `or` for the winter months.

**Examples:**
```
Enter a month (1-12): 7
Season: Summer
```
```
Enter a month (1-12): 12
Season: Winter
```

## Exercise 5: Plural Form

Ask the user to enter a number of items (zero or more). Print how many items they have, using the correct singular or plural word.

**Requirement:** Use a single ternary (conditional) expression to choose between `"item"` and `"items"`.

**Examples:**
```
Enter the number of items: 1
You have 1 item.
```
```
Enter the number of items: 3
You have 3 items.
```

## Exercise 6: Rock, Paper, Scissors

Ask two players to enter their choice: `rock`, `paper`, or `scissors`. Print the result:

- Rock beats scissors, scissors beats paper, and paper beats rock.
- If both players choose the same, print `Draw.`
- If either choice is not one of the three valid options, print `Invalid choice.`
- Otherwise, print `Player 1 wins.` or `Player 2 wins.`

**Examples:**
```
Player 1 (rock/paper/scissors): rock
Player 2 (rock/paper/scissors): scissors
Player 1 wins.
```
```Player 1 (rock/paper/scissors): paper
Player 2 (rock/paper/scissors): paper
Draw.
```

## Exercise 7: Shipping Fee

Ask the user to enter the weight of a package in kilograms and whether the delivery is express (`y` or `n`). Calculate the shipping fee:

| Weight | Base fee |
|--------|----------|
| up to 1 kg | 20 |
| over 1 kg, up to 5 kg | 35 |
| over 5 kg, up to 20 kg | 55 |

**Rules:**
- Express delivery adds 15 to the base fee.
- If the weight is zero or negative, print `Invalid weight.`
- If the weight is over 20 kg, print `Package too heavy.`

**Examples:**
```
Enter the weight (kg): 3
Express delivery? (y/n): y
Shipping fee: 50
```
```
Enter the weight (kg): 25
Express delivery? (y/n): n
Package too heavy.
```