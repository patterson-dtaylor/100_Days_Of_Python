# Tip Calculator
print("Welcome to the tip calculator.")

# Gathering total bill
total_bill = float(input("What was the total bill? "))

# Gathering tip needed
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100

# Gathering Split Num
split_num = float(input("How many people to split the bill? "))

# Gathering grand total
total_plus_tip = (total_bill * (1 + tip_percentage))

# Gathering each person's bill
split_bill = total_plus_tip / split_num

# End prompt
print(f"Each person should pay: ${split_bill:.2f}")