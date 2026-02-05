'''
Get distance_in_kilometers
distance_in_miles= distance_in_kilometers * 0.621371
print distance_in_miles
'''
distance_in_kilometers = float(input("Enter the distance in kilometers: "))
distance_in_miles = distance_in_kilometers * 0.621371
print(f"Your distance is {distance_in_miles:.2f} miles")