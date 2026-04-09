# Program to find duplicate characters in a string

# Taking input from user
text = input("Enter a string: ")

# Initialize empty list to store duplicates
duplicates = []

# Loop through each character
for ch in text:
    
    # Check if character appears more than once
    if text.count(ch) > 1 and ch not in duplicates:
        duplicates.append(ch)   # Add to duplicates list

# Display duplicates separated by space
print("Duplicate characters =", " ".join(duplicates))