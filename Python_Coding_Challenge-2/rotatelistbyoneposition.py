# Program to rotate list by one position (right rotation)

# Taking input from user
# Example input: 1 2 3
numbers = list(map(int, input("Enter elements separated by space: ").split()))

# Store last element
last = numbers[-1]

# Shift elements to right
for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]

# Place last element at first position
numbers[0] = last

# Display result
print("Rotated list =", numbers)