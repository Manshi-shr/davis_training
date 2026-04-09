# Program to reverse a number

# Taking input from user
num = int(input("Enter a number: "))

# Store original number (optional, for reference)
original = num

# Initialize reversed number
reverse = 0

# Loop until number becomes 0
while num > 0:
    
    # Get last digit
    digit = num % 10
    
    # Add digit to reversed number
    reverse = reverse * 10 + digit
    
    # Remove last digit from original number
    num = num // 10

# Display reversed number
print("Reversed number =", reverse)