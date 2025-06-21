"""String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days."""

# filename: birthday_weeks.py
from datetime import date            # 1. import the blueprint

today = date.today()                 # 2. build today's object
print(f"Today: {today} (ISO week {today.isocalendar().week})")

# 3. user input → yyyy-mm-dd
year, month, day = map(int, input("YYYY-MM-DD: ").split("-"))
birthday = date(year, month, day)    # 4. build another object

print(f"Your birthday sits in ISO week {birthday.isocalendar().week}")

# optional: how many full weeks away
weeks_left = (birthday - today).days // 7
print(f"≈ {weeks_left} week(s) until then")
