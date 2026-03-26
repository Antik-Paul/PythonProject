def main():
    '''takes inputs, prints style and calls function'''
    coffee_yield = float(input("Yeild (in grams): "))
    dose = float(input("Dose (in grams): "))
    ratio = calculate_ratio(coffee_yield, dose)
    style = coffee_style(ratio)
    print(f"1:{ratio:.1f} is considered {style}")

def coffee_style(ratio):
    '''checks coffee style'''
    if ratio <= 1.0:
        return "Ristretto"
    elif ratio >= 2.0 and ratio <= 3.0:
        return "Normale"
    else:
        return "Lungo"
    
def calculate_ratio(coffee_yield, dose):
    '''calculates ratio'''
    ratio = coffee_yield / dose
    return ratio

def check_coffee():
    """Test coffee style function."""
    style = coffee_style(1)
    print(f"coffee_style(1), expected ristretto, got {style}")

    style = coffee_style(2)
    print(f"coffee_style(2), expected normale, got {style}")

    style = coffee_style(13.5)
    print(f"coffee_style(13.5), expected lungo, got {style}")

    style = coffee_style(1.9)
    print(f"coffee_style(1.9), expected ristretto, got {style}")

    style = coffee_style(2.5)
    print(f"coffee_style(2.5), expected normale, got {style}")

    style = coffee_style(3.5)
    print(f"coffee_style(3.5), expected lungo, got {style}")

main()

'''
 Pseudocode for whole program:
 function main()
     dose = get valid number
     coffee_yield = get valid number
     ratio = calculate ratio
     style = determine coffee style
     print ratio and style

 Pseudocode for coffee style function:
 function determine_coffee_style(ratio)
     if ratio < 2
         return ristretto
     if ratio < 3
         return normale
     return lungo
'''