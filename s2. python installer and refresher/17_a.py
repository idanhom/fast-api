"""String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days."""

from datetime import date

birthday_input = input("When's your birthday? (as mm-dd) " )
month, day = map(int, birthday_input.split("-"))

# after having year-month-day as str
# i want to know where in the calendar this sits

week = date(2024, month, day).isocalendar().week

print(f"Your birthday sits at week 47 this year.")
