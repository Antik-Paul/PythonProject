#Tax (with pseudocode)

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
DISPLAY total_tax
DISPLAY take_home_pay
'''
TAX_RATE_LOW = 0.02  # 2%
TAX_RATE_MID = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_MID = 500
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))

if income < 0 :
    print("Error: Income cannot be negative")
else:
    if income < TAX_THRESHOLD_LOW :
        tax_rate = 0
    elif income <= TAX_THRESHOLD_MID :
        tax_rate = TAX_RATE_LOW
    elif income <= TAX_THRESHOLD_HIGH :
        tax_rate = TAX_RATE_MID
    else :
        tax_rate = TAX_RATE_HIGH

    total_tax = income * tax_rate
    take_home_pay = income - total_tax

print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")


#Car Insurance

applicant_age = float(input("What's your age : "))

if applicant_age < 18:
    print("Hire refused")
elif applicant_age < 25:
    print("Insurance Required")
else:
    print("Insurance not required")


#Simple Password Checker

secret_password = "Hashbrown_with_syrup"

guess = input("Enter the secret password: ")

if guess == secret_password:
    print("Access granted")
else:  
    print("Access denied")


#Basketball

number_of_shots_attemted = int(input("Number of shots attempted: "))
number_of_shots_made = int(input("Number of shots made: "))

shooting_percenatge = (number_of_shots_made/number_of_shots_attemted)*100

print(f'Your Shooting percentage is {shooting_percenatge}')

if shooting_percenatge >= 50:
    print("That's great!")


#Rock of Ages

age = int(input("Enter your age: "))

if age < 0 or age > 120 :
    print("invalid age")

else :
    if age < 13 :
        print("Enjoy the fun life")
    elif age < 20 :
        print("Explore and find a way to grow and discover")
    elif age < 65 :
        print("Work for the better future")
    else :
        print("Enjoy your life with your kids and grandkids")



#Speeding Fines

user_current_speed = float(input("Enter your speed: "))
road_speed_limit = float(input("Enter the speed limit: "))

speed_over_limit = user_current_speed - road_speed_limit 

if speed_over_limit <= 0 :
    your_fine = 0
elif speed_over_limit < 11 :
    your_fine = 322
elif speed_over_limit <= 20 :
    your_fine = 483
elif speed_over_limit <= 30 :
    your_fine = 725
elif speed_over_limit <= 40 :
    your_fine = 1209
else :
    your_fine = 1854

if your_fine == 0 :
    print("You don't need to fill any fines")
else :
    print(f'Your fine is ${your_fine}')