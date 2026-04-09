# Program to count number of digits in a number

# Taking input from user
num = int(input("Enter a number: "))

# Initialize counter
count = 0

# Handle case when number is 0
if num == 0:
    count = 1
else:
    # Loop until number becomes 0
    while num > 0:
        count += 1           # Increase count
        num = num // 10      # Remove last digit

# Display result
print("Number of digits =", count)