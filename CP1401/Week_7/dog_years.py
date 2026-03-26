def main():
    '''Takes age, prints dog years'''
    age = float(input("Human years: "))

    while age >= 0:
        dog_age = calculate_dog_years(age)
        print(f"Dog years: {dog_age}")
        age = float(input("Human years: "))


def calculate_dog_years(human_years):
    """Convert human years to dog years."""
    if human_years <= 2:
        return human_years * 10.5
    return 21 + 4 * (human_years - 2)


main()