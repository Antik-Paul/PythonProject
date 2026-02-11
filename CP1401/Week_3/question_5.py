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
