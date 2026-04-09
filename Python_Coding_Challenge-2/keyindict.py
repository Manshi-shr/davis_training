# Program to check if a key exists in a dictionary

# Example dictionary
data = {"a": 1, "b": 2}

# Taking key input from user
key = input("Enter key to search: ")

# Check if key exists
if key in data:
    print("Yes")    # Key exists
else:
    print("No")     # Key does not exist