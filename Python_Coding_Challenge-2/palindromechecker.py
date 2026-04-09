# Program to check whether a number is palindrome

# Taking input from user
num = int(input("Enter a number: "))

# Store original number
original = num

# Initialize reversed number
reverse = 0

# Reverse the number using loop
while num > 0:
    
    digit = num % 10          # Get last digit
    reverse = reverse * 10 + digit   # Build reversed number
    num = num // 10           # Remove last digit

# Check if original and reversed are same
if original == reverse:
    print("Palindrome")       # If same
else:
    print("Not Palindrome")   # If different