#to calculate total bill
units = int(input("Enterthe consumed units: "))

# Slabs: (limit, rate)
slabs = [(100, 5), (100, 7), (float('inf'), 10)]

bill = 0

for limit, rate in slabs:
    used = min(units, limit)
    bill += used * rate
    units -= used
    if units <= 0:
        break
#displaying output
print("Total bill:", bill)