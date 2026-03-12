yiel = float(input("Yeild (in grams): "))
dose = float(input("Dose (in grams): "))

def main():
    coffee_style(calculate_ratio(yiel, dose))

def coffee_style(ratio):
    print(f'1:{ratio:.2f} is considered a ', end="")
    if ratio <= 1.0:
        print("Ristretto")
    elif ratio >= 2.0 and ratio <= 3.0:
        print("Normale")
    else:
        print("Lungo")
    
def calculate_ratio(yiel, dose):
    ratio = yiel / dose
    return ratio

main()