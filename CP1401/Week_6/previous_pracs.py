"""4. Add Functions to Previous Pracs"""


def main():
    """Run previous practical exercises with functions."""
    print("Salary for worker level")
    worker_level = int(input("Worker level (1-10): ", 1, 10))
    salary = calculate_salary(worker_level)
    print(f"Salary is ${salary:.2f}")

    print("\nPrint grid")
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    print_grid(int(rows), int(columns))


def calculate_salary(worker_level):
    """Calculate salary from worker level."""
    return worker_level * 5000


def print_grid(rows, columns):
    """Print a grid with row numbers."""
    for i in range(rows):
        for j in range(columns):
            print(j,end=" ")
        print()

main()