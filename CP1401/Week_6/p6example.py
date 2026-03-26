def main():
    """Get details, calculate BMI and display result."""
    height = get_valid_number("Height (m): ", 0, 3)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    age = get_valid_number("Age: ", 0, 120)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"At age {age:.0f}, this BMI is {bmi:.1f}, which is considered {category}")


def run_tests():
    """Test program functions."""
    bmi = calculate_bmi(2, 60)
    print(f"calculate_bmi(2, 60), expected 15.0, got {bmi}")

    bmi = calculate_bmi(1.5, 100)
    print(f"calculate_bmi(1.5, 100), expected 44.444..., got {bmi}")

    print(f"determine_weight_category(16.5), expected underweight, got {determine_weight_category(16.5)}")
    print(f"determine_weight_category(18.5), expected normal, got {determine_weight_category(18.5)}")
    print(f"determine_weight_category(25), expected overweight, got {determine_weight_category(25)}")
    print(f"determine_weight_category(30), expected obese, got {determine_weight_category(30)}")


def calculate_bmi(height, weight):
    """Calculate BMI from height and weight."""
    return weight / (height ** 2)


def determine_weight_category(bmi):
    """Determine BMI category."""
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obese"


def get_valid_number(prompt, low, high):
    """Get a valid number between low and high inclusive."""
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


run_tests()
main()