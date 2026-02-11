user_current_speed = float(input("Enter your speed: "))
road_speed_limit = float(input("Enter the speed limit: "))

speed_over_limit = user_current_speed - road_speed_limit 

if speed_over_limit <= 0 :
    your_fine = 0
elif speed_over_limit < 11 :
    your_fine = 322
elif speed_over_limit <= 20 :
    your_fine = 483
elif speed_over_limit <= 30 :
    your_fine = 725
elif speed_over_limit <= 40 :
    your_fine = 1209
else :
    your_fine = 1854

if your_fine == 0 :
    print("You don't need to fill any fines")
else :
    print(f'Your fine is ${your_fine}')