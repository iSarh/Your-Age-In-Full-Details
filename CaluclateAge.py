# This is a sample Python script.
print(" Calculate your age ".center(80,'#'))

age =int( input("what\'s your age? ").strip())
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
mins = hours * 60
sec = mins * 60

print ("\nyou lived for: ")
print(f"{months} months.")
print(f"{weeks} weeks.")
print(f"{days:,} days.")
print(f"{hours:,} hours.")
print(f"{mins:,} minutes.")
print(f"{sec:,} seconds.")
