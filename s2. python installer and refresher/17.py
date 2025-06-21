"""String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days."""

from datetime import date

# 1. Build a 'today' object from the date class
today = date.today()
print(f"Today is {today}")                # --> 2025-06-21 (for example)

# 2. Ask that object to do something: report its ISO week number
today_week = today.isocalendar().week
print(f"Today sits in week {today_week}\n")

# 3. Get a birthday from the user
birthday_input = input("Enter your birthday (dd-mm-yyyy): ")
day, month, year = map(int, birthday_input.split("-"))

# 4. Use the recipe again to bake a second object, this time your birthday
birthday_date = date(year, month, day)

# 5. Ask *that* object the same question
birthday_week = birthday_date.isocalendar().week
print(f"Your birthday falls in week {birthday_week}")
