 #to calculate electricity bill

# Taking input
units = int(input("Enter units consumed: "))

# Calculating bill based on conditions
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# Display result
print("Total bill amount is:", bill)