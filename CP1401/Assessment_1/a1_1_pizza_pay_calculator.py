print("Warm Pizza Pay Calculator")

PAY_PER_TRIP = 1.45
PAY_PER_MINUTE = 0.95

number_of_trips = int(input("number of trips: "))
number_of_minutes = int(input("number of minutes: "))

total_pay_of_trips = PAY_PER_TRIP * number_of_trips
total_pay_of_minutes = PAY_PER_MINUTE * number_of_minutes

total_pay = total_pay_of_minutes + total_pay_of_trips

print(f'For {number_of_trips} trips, your pay is: $ {total_pay_of_trips:.2f}')
print(f'For {number_of_minutes} minutes, your pay is: $ {total_pay_of_minutes:.2f}')
print(f'Your total pay is ${total_pay:.2f}')