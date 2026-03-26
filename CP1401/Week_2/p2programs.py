#Discount Price
original_price= float(input("Give the origin price: "))

discount= original_price * 0.2
new_price= original_price - discount

print("The new price is: ", new_price)


#Kilometres to Miles (with pseudocode)
'''
GET distance_in_kilometers
distance_in_miles= distance_in_kilometers * 0.621371
DISPLAY distance_in_miles
'''
distance_in_kilometers = float(input("Enter the distance in kilometers: "))
distance_in_miles = distance_in_kilometers * 0.621371

print(f"Your distance is {distance_in_miles:.2f} miles")


#Holiday Cost (with pseudocode)
'''
daily_hotel_cost=75
GET daily_food_cost
GET daily_activities_cost
GET number_of_days
total_cost=(daily_food_cost+daily_activities_cost+daily_hotel_cost)*number_of_days
DISPLAY total_cost
'''
daily_hotel_cost = 75

daily_food_cost = float(input("Enter the food cost: "))
daily_activities_cost = float(input("Enter the activities cost: "))
number_of_days = int(input("Enter the number of days: "))

total_cost = (daily_food_cost+daily_activities_cost+daily_hotel_cost)*number_of_days

print(f"Your total cost is {total_cost:.2f} ")



#Deep Sleep Calculation
total_sleep = int(input("Total sleep in seconds: "))
deep_sleep = int(input("Deep sleep in seconds : "))

percentage = deep_sleep / total_sleep

print(F'Deep Sleep = {deep_sleep//60}m {deep_sleep%60}s')
print(F'Total Sleep = {total_sleep//60}m {total_sleep%60}s')
print(f'Percentage = {percentage*100}%')