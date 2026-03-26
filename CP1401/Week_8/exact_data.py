record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]

print(f"Last name: {record[1]}")
print(f"Born: {record[2]}")

year = record[2][2]
print(f"{record[0]} was born in {year} and was a great {record[3]} player.")


# Test with another record
record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]

print(f"\nLast name: {record[1]}")
print(f"Born: {record[2]}")

year = record[2][2]
print(f"{record[0]} was born in {year} and was a great {record[3]} player.")