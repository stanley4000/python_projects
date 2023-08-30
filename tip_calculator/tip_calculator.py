print("Welcome to the tip calculator.")
total = int(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
pay = (total + (total * .01 * percent)) / people
print(f"Each person should pay: ${pay}")
