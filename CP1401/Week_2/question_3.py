'''
daily_hotel_cost=75
Get daily_food_cost
Get daily_activities_cost
Get number_of_days
total_cost=(daily_food_cost+daily_activities_cost+daily_hotel_cost)*number_of_days
print total_cost
'''
daily_hotel_cost = 75

daily_food_cost = float(input("Enter the food cost: "))
daily_activities_cost = float(input("Enter the activities cost: "))
number_of_days = int(input("Enter the number of days: "))

total_cost = (daily_food_cost+daily_activities_cost+daily_hotel_cost)*number_of_days

print(f"Your total cost is {total_cost:.2f} ")
