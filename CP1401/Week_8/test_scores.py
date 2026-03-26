"""
Pseudocode
get scores
for each score:
    validate input (0-100)
    add to list
for each score:
    determine grade
    print result
calculate average
print average
determine trend
print trend
"""

NUMBER_OF_SCORES = 4

def main():

    scores = []

    for i in range(NUMBER_OF_SCORES):
        score = float(input(f"Score {i + 1}: "))
        while score < 0 or score > 100:
            print("Invalid score")
            score = float(input(f"Score {i + 1}: "))
        scores.append(score)

    total = 0

    for i in range(len(scores)):
        grade = get_grade(scores[i])
        print(f"Score {i + 1} was {scores[i]:6.1f}, which is {grade}")
        total += scores[i]

    average = total / NUMBER_OF_SCORES
    print(f"The average score was {average}")

    if scores[-1] > average:
        print("The trend is positive")
    else:
        print("The trend is not positive")


def get_grade(score):
    '''It checks the grade'''
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "F"


main()