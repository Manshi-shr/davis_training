#to calculate the total bill of electricity
#taking input form the user
units = int(input("Enter the consumed units: "))

slabs = {100: 5, 200: 7}
bill = 0
prev = 0

for limit, rate in slabs.items():
    if units > limit:
        bill += (limit - prev) * rate
        prev = limit
    else:
        bill += (units - prev) * rate
        break
else:
    bill += (units - prev) * 10
#displaying total bill
print("Total bill:", bill)