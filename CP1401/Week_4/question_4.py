#A.Sentinal

SENTINEL = -1
totalA = 0
countA = 0

age = int(input("Enter age (-1 to finish): "))

while age != SENTINEL :
    totalA = totalA + age
    countA += 1
    age = int(input("Enter age (-1 to finish): "))

if countA > 0 :
    average = totalA / countA
    print(average)
else:
    print("No ages were entered.")


#B. Ask-the-user-to-quit

smiley_count = 0
frowny_count = 0

choice = input("(S)miley\n(F)rowny\n(Q)uit\n").lower()

while choice != 'q':
    if choice == 's':
        print(":)")
        smiley_count += 1
    elif choice == 'f':
        print(":(")
        frowny_count += 1
    else:
        print("Invalid choice")

    choice = input("\n(S)miley\n(F)rowny\n(Q)uit\n").lower()

print("Farewell")
print("You printed ", smiley_count , " smileys")
print("You printed ", frowny_count , " frownys")


#C. Definite count

totalC = 0

countC = int(input("How many numbers do you want to add up? : "))

for i in range(1, countC+1):
    number = int(input(f"Enter number {i}: "))
    totalC += number 

print(f"The total of those {countC} numbers is {totalC}") 