# Program to count number of words in a sentence

# Taking input from user
text = input("Enter a sentence: ")

# Split sentence into words
words = text.split()

# Count number of words
count = len(words)

# Display result
print("Number of words =", count)