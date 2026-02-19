for i in range(1 , 101 , 2):
    print(i , sep="")

for i in range(1896 , 2027 , 4):
    print(i , end=" ")

password = input("enter a password")

while password != "python123":
    password = input("Enter the password: ")