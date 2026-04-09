# Program to find maximum value in a list without using max()

# Taking list input from user
# Example input: 5 8 2
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Assume first element is maximum
maximum = numbers[0]

# Loop through list
for num in numbers:
    
    # Compare each element with current maximum
    if num > maximum:
        maximum = num   # Update maximum

# Display result
print("Maximum value =", maximum)