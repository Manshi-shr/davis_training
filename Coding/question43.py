#to calculate the total bill of electricity
units = int(input("Enter units: "))
bill = 0

match units:
    case u if u <= 100:
        bill = u * 5
    case u if u <= 200:
        bill = 100 * 5 + (u - 100) * 7
    case _:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Total bill amount:", bill)