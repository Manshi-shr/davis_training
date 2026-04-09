# Program to check if two strings are anagrams

# Taking input from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase for proper comparison
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Sort both strings and compare
if sorted(str1) == sorted(str2):
    print("True")   # Strings are anagrams
else:
    print("False")  # Not anagrams