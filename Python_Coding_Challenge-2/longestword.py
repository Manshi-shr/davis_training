# Program to find the longest word in a sentence

# Taking input from user
text = input("Enter a sentence: ")

# Split sentence into words
words = text.split()

# Assume first word is longest
longest = words[0]

# Loop through each word
for word in words:
    
    # Compare lengths
    if len(word) > len(longest):
        longest = word   # Update longest word

# Display result
print("Longest word =", longest)