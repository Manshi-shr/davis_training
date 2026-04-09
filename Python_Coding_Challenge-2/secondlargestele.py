# Program to find second largest element in a list

# Taking input from user
# Example input: 10 20 5 15
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Remove duplicates to handle cases like [10, 10, 20]
unique_numbers = list(set(numbers))

# Assume first element as largest and second largest
largest = second_largest = unique_numbers[0]

# Find largest element
for num in unique_numbers:
    if num > largest:
        largest = num

# Find second largest element
second_largest = None
for num in unique_numbers:
    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num

# Display result
print("Second largest =", second_largest)