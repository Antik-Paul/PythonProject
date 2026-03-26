import random

quantity = int(input("How many random numbers: "))
maximum = int(input("Maximum number: "))

numbers = []

for i in range(quantity):
    numbers.append(random.randint(0, maximum))

print("The numbers are:", numbers)
print("The minimum is", min(numbers))
print("The maximum is", max(numbers))

random_index = random.randint(0, len(numbers) - 1)
print("A randomly chosen number is", numbers[random_index])

reversed_numbers = numbers.copy()
reversed_numbers.reverse()
print("The numbers reversed are", reversed_numbers)

sorted_numbers = sorted(numbers)
print("The numbers sorted are", sorted_numbers)