SECRET = 6
count = 0

guess = int(input("Guess a number: "))

while guess != SECRET:
    print("Guess again!")
    count+=1
    guess = int(input("Guess a number: "))
print("You got it in ", count, " guesses." )