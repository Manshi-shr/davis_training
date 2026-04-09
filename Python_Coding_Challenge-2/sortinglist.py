# Program to sort a list without using sort()

# Taking input from user
# Example input: 3 1 2
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Using simple Bubble Sort logic
n = len(numbers)

# Outer loop for passes
for i in range(n):
    
    # Inner loop for comparison
    for j in range(0, n - i - 1):
        
        # Swap if elements are in wrong order
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

# Display sorted list
print("Sorted list =", numbers) 