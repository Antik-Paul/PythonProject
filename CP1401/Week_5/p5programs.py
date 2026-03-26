# 1.Percentage program (I, P, O)

'''
Pseudocode:
Take original
Take change
result = 0
If change is less than 0
    result = original - (original * change)
    Display the original, change and result in one statement
else
    result = original + (original * change)
    Display the original, change and result in one statement
'''
original = float(input("Enter the Original Number: "))
change = float(input("Enter the change you want:"))

result=0

if change < 0:
    result = original - (original * change)
    print(f'Original: {original}, Change: {change}, Result: {result}')
else:
    result = original + (original * change)
    print(f'Original: {original}, Change: {change}, Result: {result}')


# 2.Time of day (Decision)

'''
Take hour
Take direction
If hour is smaller than 12, time is before noon
else time is after noon

If direction is coming, message is Hi!
Else if direction is going, message is Bye!

Display the time and the direction with the message
'''

hour = int(input("Time of the day(0-23): "))
direction = input("Are you coming or going? :").lower()

if hour < 12 :
    time = "before noon"
else:
    time = "after noon"

if direction == "coming":
    message = "Hi!"
elif direction == "going":
    message = "Bye!"

print(f'It is {time} and you are {direction}. {message}')



# 3.Coffee orders (Decision)

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



# 4.Coffee orders with error-checking (Repetition)

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



# 5. Accumulation (Repetition)

'''
Take the high limit
Take the low limiit

While the lower limit is greater than high limit 
    Display invalid inputs
    Take high limit
    Take low limit

total=0

For each number from the low limit to high limit
    Display the number in the sameline 
    add the number in the total
Display the total
'''

high_limit = int(input("High Limit: "))
low_limit = int(input("Low Limit: "))

while low_limit > high_limit :
    print("invalid inputs")
    high_limit = int(input("High Limit: "))
    low_limit = int(input("Low Limit: "))

total = 0

for i in range(low_limit,high_limit+1):
    print(i,end=" ")
    total += i
print(f'Totals: {total}')



# 6. Debugging (code and test values)

age = int(input("Age: "))
if age < 18:
    print("Entry refused")
elif age < 30:
    print("Limited entry allowed")
else:
    print("Full entry allowed")

# Tests: 
# (Input, Expected, Actual outcomes)
# 15, Entry refused, Entry refused
# 17, Entry refused, Entry refused
# 22, Limited entry allowed, Limited entry allowed
# 29, Limited entry allowed, Limited entry allowed
# 31, Full entry allowed, Full entry allowed
# Problem found in original code:
# Age 30 produced no output because the last condition was "age > 30"
# instead of covering age 30 as well.
#
# Fix made:
# Replaced "elif age > 30" with "else"