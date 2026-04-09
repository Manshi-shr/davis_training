# Program to count frequency of elements using dictionary

# Taking input from user
# Example input: 1 2 2 3
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize empty dictionary
freq = {}

# Loop through list
for num in numbers:
    
    # If element already exists, increase count
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1   # Initialize count as 1

# Display result
print("Frequency =", freq)