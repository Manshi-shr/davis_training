# Program to find common elements between two lists

# Taking input for first list
list1 = list(map(int, input("Enter first list elements: ").split()))

# Taking input for second list
list2 = list(map(int, input("Enter second list elements: ").split()))

# Initialize empty list to store common elements
common = []

# Loop through first list
for num in list1:
    
    # Check if element is present in second list and not already added
    if num in list2 and num not in common:
        common.append(num)

# Display result
print("Common elements =", common)