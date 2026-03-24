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