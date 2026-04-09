# mymodule.py

# Function to add two numbers
def add(a, b):
    return a + b   # Return sum
# Main program to use the module

# Import the module
import mymodule

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call function from module
result = mymodule.add(num1, num2)

# Display result
print("Sum =", result)