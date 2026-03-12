input_number = int(input("Enter a number: "))
def main():
    parity_checker(input_number)

def parity_checker(input_number):
    parity = input_number % 2
    print(f'Parity of {input_number} should be: {input_number%2}, got: {parity}')

main()
