#to calculate the bill
units = int(input("Enter the consumed  units: "))

slabs = [(100, 5), (100, 7), (units, 10)]

used = [min(units, s[0]) for s in slabs]
units -= sum(used[:2])

bill = used[0]*5 + used[1]*7 + max(0, units)*10
#displaying total bill
print("Total bill:", bill)