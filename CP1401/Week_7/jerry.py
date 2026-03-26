def main():
    speed_in_miles = get_valid_number("Speed in miles: ")
    speed_limit_in_kilometres = get_valid_number("speed limit in kilometres: ")
    speed_in_kilometres = convert_miles_to_kilometres(speed_in_miles)
    amount_over_limit = speed_in_kilometres - speed_limit_in_kilometres
    fine = determine_fine(amount_over_limit)
    print(f'Your fine is ${fine}')

def get_valid_number(input_number):
    """Get a valid positive number."""
    number = float(input(input_number))
    while number < 0:
        print("Invalid input")
        number = float(input(input_number))
    return number

def convert_miles_to_kilometres(miles):
    """Convert miles to kilometres."""
    return miles * 1.609

def determine_fine(speed_over_limit):
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

    return your_fine

main()