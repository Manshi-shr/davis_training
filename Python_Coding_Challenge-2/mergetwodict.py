# Program to merge two dictionaries

# Example dictionaries
dict1 = {"a": 1}
dict2 = {"b": 2}

# Create new dictionary
merged_dict = {}

# Add elements of first dictionary
for key in dict1:
    merged_dict[key] = dict1[key]

# Add elements of second dictionary
for key in dict2:
    merged_dict[key] = dict2[key]

# Display result
print("Merged dictionary =", merged_dict)