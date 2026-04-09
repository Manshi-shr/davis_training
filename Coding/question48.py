#to calculate total bill of electricity
from functools import reduce

units = int(input("Enter units: "))

rates = [5]*100 + [7]*100 + [10]*(units-200 if units > 200 else 0)

bill = reduce(lambda x, y: x + y, rates[:units], 0)

print("Total bill:", bill)