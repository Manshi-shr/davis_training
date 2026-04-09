#to calculate total bill
def bill_calc(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + bill_calc(units - 100) - (units - 100) * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10
#taking input
units = int(input("Enter  the consumed units: "))
#displaying output
print("Total bill:", bill_calc(units))