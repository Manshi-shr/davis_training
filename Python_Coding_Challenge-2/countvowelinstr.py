# Program to count vowels in a string

# Taking input from user
text = input("Enter a string: ")

# Convert string to lowercase for uniform checking
text = text.lower()

# Initialize counter
count = 0

# Loop through each character in string
for ch in text:
    
    # Check if character is a vowel
    if ch in ('a', 'e', 'i', 'o', 'u'):
        count += 1   # Increase count

# Display result
print("Number of vowels =", count)