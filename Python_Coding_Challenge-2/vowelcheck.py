# Program to check whether a character is a vowel

# Taking input from user
ch = input("Enter a character: ")

# Convert character to lowercase to handle both cases (A/a)
ch = ch.lower()

# Checking if character is a vowel
if ch in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")        # If character is vowel
else:
    print("Not a Vowel")  # If character is not vowel