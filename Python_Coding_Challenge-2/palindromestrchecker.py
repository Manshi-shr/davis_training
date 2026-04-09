# Program to check whether a string is palindrome

# Taking input from user
text = input("Enter a string: ")

# Reverse the string using slicing
reverse = text[::-1]

# Compare original and reversed string
if text == reverse:
    print("Yes")   # It is a palindrome
else:
    print("No")    # Not a palindrome

    