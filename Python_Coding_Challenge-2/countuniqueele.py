# Program to count unique elements in a list

# Taking input from user
# Example input: 1 1 2 3 3
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Convert list to set to remove duplicates
unique_elements = set(numbers)

# Count unique elements
count = len(unique_elements)

# Display result
print("Count of unique elements =", count)