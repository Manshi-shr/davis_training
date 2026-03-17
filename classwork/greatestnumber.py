num = int(input("Enter a number: "))

max_digit = 0

for digit in num:
    if int(digit) > max_digit:
        max_digit = int(digit)

print("Greatest digit is:", max_digit)