# Program to convert string to uppercase without using upper()

# Taking input from user
text = input("Enter a string: ")

# Initialize empty string
result = ""

# Loop through each character
for ch in text:
    
    # Check if character is lowercase (a-z)
    if 'a' <= ch <= 'z':
        
        # Convert to uppercase using ASCII values
        # ord(ch) gives ASCII of character
        # chr() converts ASCII back to character
        result += chr(ord(ch) - 32)
    else:
        result += ch   # Keep character as it is

# Display result
print("Uppercase string =", result)