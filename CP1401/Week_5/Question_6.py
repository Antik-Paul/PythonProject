age = int(input("Age: "))
if age < 18:
    print("Entry refused")
elif age < 30:
    print("Limited entry allowed")
else:
    print("Full entry allowed")

# Tests: 
# (Input, Expected, Actual outcomes)
# 15, Entry refused, Entry refused
# 17, Entry refused, Entry refused
# 22, Limited entry allowed, Limited entry allowed
# 29, Limited entry allowed, Limited entry allowed
# 31, Full entry allowed, Full entry allowed
# Problem found in original code:
# Age 30 produced no output because the last condition was "age > 30"
# instead of covering age 30 as well.
#
# Fix made:
# Replaced "elif age > 30" with "else"