# Program to remove duplicates from a list

# Taking input from user
# Example input: 1 1 2 3
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize empty list to store unique elements
unique_list = []

# Loop through each element
for num in numbers:
    
    # Check if element is not already in unique_list
    if num not in unique_list:
        unique_list.append(num)   # Add unique element

# Display result
print("List without duplicates =", unique_list)