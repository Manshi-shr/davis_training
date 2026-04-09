# Program to count occurrences of a character in a string

# Taking input from user
text = input("Enter a string: ")
char = input("Enter character to count: ")

# Initialize counter
count = 0

# Loop through string
for ch in text:
    
    # Check if character matches
    if ch == char:
        count += 1

# Display result
print("Count =", count)