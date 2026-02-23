"""
CP1401 2026 TR1 Assignment 1
Program – Sleep Tracker
Name: Antik Paul
Date started: 23/02/2026
Pseudocode:
DISPLAY Sleep Tracker

total_sleep_hours = 0

For day in range 1 to 5
    GET sleep_hours
    total_sleep_hours = total_sleep_hours + sleep_hours
    If sleep_hours is less than 0 or greater than 24
        DISPLAY Invalid numbers of hours.
        GET sleep_hours

DISPLAY Recommended total sleep is: 40
DISPLAY Your total hours of sleep is: total_sleep_hours

average_sleep_hours = total_sleep_hours / 5
sleep_debt = 40 - total_sleep_hours

If sleep_debt is greater than 0
    DISPLAY Your sleep debt over this time is: sleep_debt
Else
    DISPLAY You are getting enough sleep. Keep it up!
"""


print("Sleep Tracker")

total_sleep_hours = 0

for day in range(1,6):
    sleep_hours = float(input(f"Night {day} hours sleep: "))
    total_sleep_hours += sleep_hours
    if sleep_hours < 0 or sleep_hours > 24 :
        print("Invalid numbers of hours.")
        sleep_hours = float(input(f"Night {day} hours sleep: "))

print("Recommended total sleep is: 40")
print(f"Your total hours of sleep is: {total_sleep_hours}")
average_sleep_hours = total_sleep_hours / 5
sleep_debt = 40 - total_sleep_hours

if sleep_debt > 0 :
    print(f'Your sleep debt over this time is: {sleep_debt}')
else:
    print("You are getting enough sleep. Keep it up!")