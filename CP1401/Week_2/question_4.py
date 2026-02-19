total_sleep = int(input("Total sleep in seconds: "))
deep_sleep = int(input("Deep sleep in seconds : "))

percentage = deep_sleep / total_sleep

print(F'Deep Sleep = {deep_sleep//60}m {deep_sleep%60}s')
print(F'Total Sleep = {total_sleep//60}m {total_sleep%60}s')
print(f'Percentage = {percentage*100}%')