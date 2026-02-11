applicant_age = float(input("What's your age : "))
if applicant_age < 18:
    print("Hire refused")
elif applicant_age < 25:
    print("Insurance Required")
else:
    print("Insurance not required")
