MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12

birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

while birth_month < MINIMUM_MONTH or birth_month > MAXIMUM_MONTH:
    print("Invalid month")
    birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

for i in range(MINIMUM_MONTH, birth_month + 1):
    print(i, end=" ")
print()

# Determine first or second half of the year
if birth_month <= MAXIMUM_MONTH / 2:
    print("Your birth month is in the first half of the year")
else:
    print("Your birth month is in the second half of the year")