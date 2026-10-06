"""
Lesson 07 - Strings
Fachinformatiker Anwendungsentwicklung - Python Roadmap
"""

# ==================================================
# Part 1: Creating Strings with f-Strings
# ==================================================

name = "Ngoc"
age = 25

# Old way: concatenate strings using the + operator.
# This works, but it becomes difficult to read when many variables are involved.
greeting_old = "Hello " + name + ", you are " + str(age) + " years old"

# Modern way: use an f-string.
# Add the letter 'f' before the quotation marks and place variables inside {}.
greeting_new = f"Hello {name}, you are {age} years old"

print(greeting_old)
print(greeting_new)

# You can also evaluate expressions directly inside {}.
print(f"Next year you will be {age + 1} years old")

# Format numbers inside an f-string.
# :.2f means "display the number with 2 decimal places".
price = 19.98765
print(f"Price: {price:.2f} EUR")

# --- Additional format specs (useful for reports / tables later) ---

# Thousand separator: ':,' inserts a comma every 3 digits.
big_number = 1234567
print(f"{big_number:,}")          # '1,234,567'

# Combine thousand separator with decimals.
salary = 45000.5
print(f"{salary:,.2f} EUR")       # '45,000.50 EUR'

# Alignment and width: useful when printing tables in the console.
# '<' left-align, '>' right-align, '^' center-align, number = total width.
label = "Name"
value = "Ngoc"
print(f"{label:<10}{value:>10}")  # left pad / right pad within 10 chars

# Fill character can be combined with alignment: fill '-', center-align, width 20.
print(f"{'TITLE':-^20}")          # '-------TITLE--------'

# ==================================================
# Part 2: String Slicing
# ==================================================

text = "Fachinformatiker"

# Slice from index 0 up to (but not including) index 5.
print(text[0:5])      # "Fachi"

# If the start index is omitted, Python starts from the beginning.
print(text[:4])       # "Fach"

# If the end index is omitted, Python continues to the end of the string.
print(text[4:])       # "informatiker"

# Negative indexes count from the end of the string.
print(text[-4:])      # "iker"

# The third value is the step.
# A step of 2 means "take every second character".
print(text[::2])

# A negative step reverses the string.
print(text[::-1])     # "rekitamrofnihcaF"

# ==================================================
# Part 3: Common String Methods
# ==================================================

raw_input = "  Nguyen Ngoc  "

# strip() removes leading and trailing whitespace.
# It does NOT remove spaces in the middle of the string.
clean_name = raw_input.strip()
print(f"'{clean_name}'")  # 'Nguyen Ngoc'

# split() breaks a string into a list, based on a separator.
# If no separator is given, it splits on whitespace by default.
full_name = "Nguyen Ngoc Tran"
parts = full_name.split(" ")
print(parts)  # ['Nguyen', 'Ngoc', 'Tran']

# join() does the opposite of split(): it combines a list into one string,
# placing the given separator between each item.
joined = "-".join(parts)
print(joined)  # 'Nguyen-Ngoc-Tran'

# upper() / lower() change the case of all letters in the string.
# Useful for normalizing data before comparison.
email = "Ngoc@Example.COM"
print(email.lower())  # 'ngoc@example.com'

# replace(old, new) substitutes every occurrence of "old" with "new".
sentence = "I am learning Java"
print(sentence.replace("Java", "Python"))  # 'I am learning Python'

# --- Additional methods commonly needed for input validation ---

filename = "report_2026.pdf"

# startswith() / endswith() check the beginning / end of a string.
print(filename.startswith("report"))   # True
print(filename.endswith(".pdf"))       # True

# find() returns the index of the first match, or -1 if not found.
# index() does the same but raises an error if not found (use with try/except).
print(filename.find("2026"))           # 7
print(filename.find("docx"))           # -1

# count() returns how many times a substring appears.
text_sample = "banana"
print(text_sample.count("a"))          # 3

# isdigit() / isalpha() / isalnum() check the character composition.
# Useful for validating raw user input before converting types.
user_age = "25"
user_name = "Ngoc"
print(user_age.isdigit())              # True -> safe to int(user_age)
print(user_name.isalpha())             # True -> letters only
print("Ngoc25".isalnum())              # True -> letters and/or digits only

# --- Exercise: cleaning and parsing raw location data ---
raw_data = "  Ho Chi Minh City, Vietnam  "

# Step 1: remove the extra whitespace around the whole string.
clean_data = raw_data.strip()

# Step 2: split into city and country using "," as the separator.
city, country = clean_data.split(",")

# Step 3: strip() each part again, because split() does not remove
# the whitespace that sits right next to the comma.
city = city.strip()
country = country.strip()

print(city.upper())  # "HO CHI MINH CITY"
print(country)        # "Vietnam"

# ==================================================
# Part 4: String Comparison
# ==================================================

# Strings are compared lexicographically: character by character,
# based on each character's Unicode code point.
print("apple" == "apple")   # True -> identical strings
print("apple" == "Apple")   # False -> comparison is case-sensitive

# When comparing with < or >, Python compares characters one by one
# until it finds a difference.
print("apple" < "banana")   # True -> 'a' comes before 'b'
print("Apple" < "apple")    # True -> uppercase letters have lower
                             # Unicode values than lowercase letters

# Because comparison is case-sensitive, it's common practice to
# normalize both sides with lower() (or upper()) before comparing
# user input.
user_input = "Munich"
target = "munich"
print(user_input.lower() == target.lower())  # True

# 'in' / 'not in' check whether a substring exists inside a string.
# This is often faster to read than find() != -1 when you only need True/False.
city_name = "Munich"
print("uni" in city_name)         # True
print("Berlin" not in city_name)  # True

# ==================================================
# Part 5: Multiline Strings and Escape Characters
# ==================================================

# Triple quotes create a multiline string, keeping line breaks as written.
# Common for docstrings, SQL queries, or email/template bodies.
email_template = """Dear Team,

This is a test email generated from a Python program.
Best regards,
Ngoc"""
print(email_template)

# Escape characters let you insert special characters inside a normal string.
# \n = newline, \t = tab, \\ = literal backslash, \" = literal double quote.
print("Line 1\nLine 2")            # newline
print("Column A\tColumn B")        # tab
print("Path: C:\\Users\\Ngoc")     # backslash
print("She said \"Hello\"")        # escaped quotes

# Raw strings (prefix 'r') ignore escape sequences entirely.
# Useful for Windows paths or regex patterns.
path = r"C:\Users\Ngoc\Documents"
print(path)  # backslashes stay literal, no need to double them
