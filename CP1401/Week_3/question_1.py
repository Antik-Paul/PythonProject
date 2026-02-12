'''
TAX_RATE_LOW = 0.05   # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000
Get Income
If income is less than 0 
    print Error: Income cannot be negative
Else
    If income is less than TAX_THRESHOLD_LOW 
        tax_rate is 0
    Else If income is less than or equal to TAX_THRESHOLD_HIGH
        tax_rate is TAX_RATE_LOW
    Else
        tax_rate is TAX_RATE_HIGH

total_tax = income * tax_rate
take_home_pay = income - total_tax
print total_tax
print take_home_pay
'''
TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))

if income < 0 :
    print("Error: Income cannot be negative")
else:
    if income < TAX_THRESHOLD_LOW :
        tax_rate = 0
    elif income <= TAX_THRESHOLD_HIGH :
        tax_rate = TAX_RATE_LOW
    else :
        tax_rate = TAX_RATE_HIGH

    total_tax = income * tax_rate
    take_home_pay = income - total_tax

print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")