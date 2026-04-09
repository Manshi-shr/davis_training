# Program to find sum of digits of a number

# Taking input from user
num = int(input("Enter a number: "))

# Initialize sum
sum_digits = 0

# Loop until number becomes 0
while num > 0:
    
    digit = num % 10          # Get last digit
    sum_digits += digit       # Add digit to sum
    num = num // 10           # Remove last digit

# Display result
print("Sum of digits =", sum_digits)