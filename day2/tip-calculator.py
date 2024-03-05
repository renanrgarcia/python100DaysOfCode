print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input(
    "What percentage tip would you like to give? 10, 12 or 15? "
)) / 100
people = int(input("How many people to split the bill? "))

tip = bill * percentage
bill_per_person = (bill + tip) / people

print(f'Each person should pay: ${bill_per_person:.2f}')
