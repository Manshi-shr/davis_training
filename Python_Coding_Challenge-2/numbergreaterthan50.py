# Program to count numbers greater than 50 in a list

# Taking list input from user
# Example input: 10 60 30 80
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize counter
count = 0

# Loop through list
for num in numbers:
    
    # Check if number is greater than 50
    if num > 50:
        count = count + 1

# Display result
print("Count =", count)