# Program to remove spaces from a string

# Taking input from user
text = input("Enter a string: ")

# Initialize empty string to store result
result = ""

# Loop through each character
for ch in text:
    
    # Check if character is not a space
    if ch != " ":
        result += ch   # Add character to result

# Display result
print("String without spaces =", result)