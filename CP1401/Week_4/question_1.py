BASE_SALARY = 5000

worker_level = int(input("Enter your worker level: "))

while worker_level < 0 or worker_level > 10:
    print("inevalid Entry")
    worker_level = int(input("Enter your worker level: "))

salary = worker_level * BASE_SALARY
print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")   