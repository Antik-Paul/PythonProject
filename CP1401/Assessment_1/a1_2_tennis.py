"""
CP1401 2026 TR1 Assignment 1
Program – Tennis Result
Name: Antik Paul
Date started: 23/02/2026
Pseudocode:
DISPLAY Welcome Player 1. How was your match?

GET player_1_score
GET opponent_score

If player_1_score is greater than opponent_score
    DISPLAY You won! :)
Else If player_1_score is less than opponent_score
    DISPLAY You lost :( Keep trying.
Else
    DISPLAY It's a draw.

total_games = player_1_score + opponent_score

If total_games is greater than or equal to 8
    DISPLAY Congratulations on playing a fast match!  
"""

print("Welcome Player 1. How was your match?")

player_1_score = int(input("Your score: "))
opponent_score = int(input("Opponent score: "))

if player_1_score > opponent_score :
    print("You won! :)")
elif player_1_score < opponent_score :
    print("You lost :( Keep trying.")
else :
    print("It's a draw.")
    
total_games = player_1_score + opponent_score

if total_games >= 8 :
    print("Congratulations on playing a fast match!")