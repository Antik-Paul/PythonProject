'''
Display the Menu
Take choice
Repeat until the choice is Q
If choice is I
    Display instructions
Else if choice is C
    Take number of products (Until Valid)
    Take price (Until Valid)
    Apply discount if number of products is greater than 5
    Display total
Else 
    Display invalid choice
'''

#Menu
print("Menu:")
print("(I)nstructions")
print("(C)alculate")
print("(Q)uit")

choice = input("Choice: ").upper()

while choice != "Q":
    if choice == "I":
        print("Enter the number of products you want to buy and your chosen price.")
        print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off")
    
    elif choice == "C":
        #Number of products count
        number_of_products = int(input("Number of Products: "))
        while number_of_products < 0:
            print("Invalid Input")
            number_of_products = int(input("Number of Products: "))

        #Price Count
        price = float(input("Price: "))
        while price < 0:
            print("Invalid Input")
            price = float(input("Price: "))

        #Discount Count
        if number_of_products > 5:
            total = number_of_products * (price * 0.9)
        else:
            total = number_of_products * price

        print(f'{number_of_products} x ${price:.2f} products = {total}')
    else:
        print("Invalid Choice")

    #Menu
    print("Menu:")
    print("(I)nstructions")
    print("(C)alculate")
    print("(Q)uit")

    choice = input("Choice: ").upper()

print("Farewell")