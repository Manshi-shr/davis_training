# Program to convert a list into a tuple

# Taking input from user
# Example input: 1 2 3
numbers = list(map(int, input("Enter elements separated by space: ").split()))

# Convert list to tuple
result = tuple(numbers)

# Display result
print("Tuple =", result)