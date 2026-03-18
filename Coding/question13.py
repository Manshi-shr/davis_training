#to calculate total electricity bill
#taking input form the user
units = int(input("Enter the consumed  units: "))
rates = [5, 7, 10]
limits = [100, 100]

bill = 0
#using range function
for i in range(len(limits)):
    if units > 0:
        used = min(units, limits[i])
        bill += used * rates[i]
        units -= used

if units > 0:
    bill += units * rates[2]
#displaying output
print("Total bill:", bill)