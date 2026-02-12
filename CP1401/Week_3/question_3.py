secret_password = "swordfish"
guess = input("Enter the secret password: ")
if guess == secret_password:
    print("Access granted")
else:  
    print("Access denied")
