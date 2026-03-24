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
