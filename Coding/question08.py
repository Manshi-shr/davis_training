#to calculate the total bill

#taking input from the user
units = int(input("Enter units consumed: "))

#applying conditionl statement to calculate the the bill
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
#displaying output
print("Total bill amount is:", bill)