number_of_shots_attemted = float(input("Number of shots attempted: "))
number_of_shots_made = float(input("Number of shots made: "))
shooting_percenatge = (number_of_shots_made/number_of_shots_attemted)*100
print(f'Your Shooting percentage is {shooting_percenatge}')
if shooting_percenatge >= 50:
    print("That's great!")
