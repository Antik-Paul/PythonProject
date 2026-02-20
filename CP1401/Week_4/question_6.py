rows = int(input("The number of rows: "))
columns = int(input("The number of columns: "))

for i in range(rows):
    for j in range(columns):
        print(j,end=" ")
    print()