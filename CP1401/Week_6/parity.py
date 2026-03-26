def main():
    '''takes input, prints the result'''
    input_number = int(input("Enter a number: "))
    parity_checker(input_number)
    print(f'{is_odd(input_number)}')

def parity_checker(input_number):
    '''checks parity'''
    parity = input_number % 2
    print(f'Parity of {input_number} should be: {input_number%2}, got: {parity}')

def is_odd(input_number):
    """Return True if number is odd, otherwise False."""
    numero = input_number % 2
    if numero == 0:
        return "False"
    else:
        return "True"

main()
