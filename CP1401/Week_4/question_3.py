print("(S)miley\n(F)rowny\n(Q)uit")

choice = input("Choose among S, F or Q: ").lower()

while choice != "q" :
    if choice == "s" :
        print(":)")
    elif choice == "f" :
        print(":(")
    else:
        print("Invalid choice")
    print("\n(S)miley\n(F)rowny\n(Q)uit")
    
    choice = input("Choose among S, F or Q: ").lower()

print("Farewell")
