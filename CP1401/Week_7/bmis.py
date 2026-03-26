def calculate_bmi(height, weight):
    """Calculate BMI."""
    return weight / (height ** 2)


def determine_weight_category(bmi):
    """Determine BMI category."""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    return "obese"


def main():
    height = 1.75

    for weight in range(50, 101, 2):
        bmi = calculate_bmi(height, weight)
        category = determine_weight_category(bmi)
        print(f"Height {height}m, Weight {weight}kg = BMI {bmi:.1f}, considered {category}")

    print()

    for h in range(150, 191, 10):
        height = h / 100
        for weight in range(50, 101, 10):
            bmi = calculate_bmi(height, weight)
            category = determine_weight_category(bmi)
            print(f"Height {height:.1f}m, Weight {weight:3}kg = BMI {bmi:.1f}, considered {category}")


main()