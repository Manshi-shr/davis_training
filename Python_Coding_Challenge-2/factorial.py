# Program to calculate factorial of a number

# Taking input from user
num = int(input("Enter a number: "))

# Initialize factorial result as 1
factorial = 1

# Check if number is negative
if num < 0:
    print("Factorial not defined for negative numbers")

else:
    # Loop from 1 to num
    for i in range(1, num + 1):
        factorial = factorial * i   # Multiply each number
    
    # Display result
    print("Factorial =", factorial)