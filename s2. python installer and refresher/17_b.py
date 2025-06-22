"""String Assignment.

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days."""


from datetime import date

starting = date(2024, 6, 22)
ending = date(2024,11,22)

birthday = (ending - starting).days

print(birthday)



