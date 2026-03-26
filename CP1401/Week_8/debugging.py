# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(len(names)):
    print(f"{i + 1}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number - 1]}")

# Problem(s) for program 1:
# Loop started at wrong index and skipped first element
# Index out of range when accessing last element

# Fixed code for program 1:
# (shown above)


# Debug program 2 - title-casing country names
countries = ["australia", "new zeaLAND", "India"]
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)

# Problem(s) for program 2:
# Tried to modify tuple, which is immutable.

# Fixed code for program 2:
# (shown above)