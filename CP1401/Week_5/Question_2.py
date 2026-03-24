'''
Take hour
Take direction
If hour is smaller than 12, time is before noon
else time is after noon

If direction is coming, message is Hi!
Else if direction is going, message is Bye!

Display the time and the direction with the message
'''

hour = int(input("Time of the day(0-23): "))
direction = input("Are you coming or going? :").lower()

if hour < 12 :
    time = "before noon"
else:
    time = "after noon"

if direction == "coming":
    message = "Hi!"
elif direction == "going":
    message = "Bye!"

print(f'It is {time} and you are {direction}. {message}')
