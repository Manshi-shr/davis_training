# Program to find missing number in a sequence

# Taking input from user
# Example input: 1 2 4 5
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Calculate expected sum using formula n(n+1)/2
n = len(numbers) + 1   # Total numbers including missing one
expected_sum = n * (n + 1) // 2

# Calculate actual sum of given numbers
actual_sum = sum(numbers)

# Missing number is difference
missing = expected_sum - actual_sum

# Display result
print("Missing number =", missing)