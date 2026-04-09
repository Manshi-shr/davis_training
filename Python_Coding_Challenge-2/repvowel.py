# Program to replace vowels with '*'

# Taking input from user
text = input("Enter a string: ")

# Initialize empty string
result = ""

# Loop through each character
for ch in text:
    
    # Check if character is a vowel
    if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
        result += "*"   # Replace vowel with *
    else:
        result += ch    # Keep character as it is

# Display result
print("Result =", result)