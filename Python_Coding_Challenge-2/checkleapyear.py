# Program to check whether a year is a leap year

# Taking input from user
year = int(input("Enter year: "))

# Leap year condition:
# 1. Year divisible by 4 AND not divisible by 100
# OR
# 2. Year divisible by 400

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")      # Condition satisfied
else:
    print("Not a Leap Year")  # Condition not satisfied