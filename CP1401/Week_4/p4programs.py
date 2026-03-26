#Error Checking

BASE_SALARY = 5000

worker_level = int(input("Enter your worker level: "))

while worker_level < 0 or worker_level > 10:
    print("inevalid Entry")
    worker_level = int(input("Enter your worker level: "))

salary = worker_level * BASE_SALARY
print(f"With worker level {worker_level}, your salary is ${salary:,.2f}") 

#Number Sequences: a, b, c

for i in range(1 , 101 , 2):
    print(i , sep="")

for i in range(1896 , 2027 , 4):
    print(i , end=" ")

password = input("enter a password")

while password != "python123":
    password = input("Enter the password: ")


#Menus (with pseudocode)

'''
print menu
get choice
while choice is not "q"
    if choice is "s"
        print smiley face
    else if choice is "f"
        print frowny face
    else
        print "Invalid choice"
    print menu
    get choice
print "Farewell"
'''

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


#Accumulation

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


#Guessing Game

SECRET = 6
count = 0

guess = int(input("Guess a number: "))

while guess != SECRET:
    print("Guess again!")
    count+=1
    guess = int(input("Guess a number: "))
print("You got it in ", count, " guesses." )


#Nested Loops

rows = int(input("The number of rows: "))
columns = int(input("The number of columns: "))

for i in range(rows):
    for j in range(columns):
        print(j,end=" ")
    print()