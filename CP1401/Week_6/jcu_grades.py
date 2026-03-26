import random
def main():
    given_score = float(input("Score: "))
    while given_score > 0 :
        print(f'The score {given_score:.1f} is {grade_checker(given_score)}')
        given_score = float(input("Score: "))
    
    number_of_scores = int(input("How many random scores: "))
    for i in range(number_of_scores):
        random_score = random.randint(0,100)
        print(f'{random_score} = {grade_checker(random_score)}')

def grade_checker(score):
    if score >= 0 and score < 50:
        return "F"
    if score >= 50 and score < 65:
        return "P"
    if score >= 65 and score < 75:
        return "C"
    if score >= 75 and score < 85:
        return "D"
    if score >= 85 :
        return "HD"

main()

    