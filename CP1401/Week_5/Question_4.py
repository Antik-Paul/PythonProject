'''
Take repeatedly for coffee type until it is white or black
Take repeatedly for Coffee size until it is small, medium or large.

If size is small, cost is 3
Else if size is medium, cost is 4
Else if size is large, cost is 5
If a user makes a mistake with either part of their order, just pick the most expensive option so the cost is 5

If colour is white, add 1 to the cost

Display the final cost

'''

coffee_type = input("Do you want a white or black coffee?: ").lower()
while coffee_type != "black" and "white":
    print("Invalid coffee type.")
    coffee_type = input("Do you want a white or black coffee?: ").lower()

coffee_size = input("Which size do you want(small, medium or large)?: ").lower()
while coffee_size != "small" and coffee_size != "medium" and coffee_size != "large":
    print("Invalid Sizing.")
    coffee_size = input("Which size do you want(small, medium or large)?: ").lower()

cost = 0

#Black Coffee Prizes:
if coffee_size == "small":
    cost = 3
elif coffee_size == "medium":
    cost = 4
elif coffee_size == "large":
    cost = 5

#White coffee prizes cost 1 dollar more from black coffee
if coffee_type == "white":
    cost += 1

print(f'Your Total Cost is: ${cost}')
