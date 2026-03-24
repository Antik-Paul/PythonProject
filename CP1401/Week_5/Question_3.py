'''
Take Coffee Type
Take Coffee size

If size is small, cost is 3
Else if size is medium, cost is 4
Else if size is large, cost is 5
If a user makes a mistake with either part of their order, just pick the most expensive option so the cost is 5

If colour is white, add 1 to the cost

Display the final cost

'''

coffee_type = input("Do you want a white or black coffee?").lower()
coffee_size = input("Which size do you want(small, medium or large)?").lower()

cost = 5

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


print(f'Cost: ${cost}')
