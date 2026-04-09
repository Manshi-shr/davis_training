# Program to sort a dictionary by keys

# Example dictionary
data = {"b": 2, "a": 1}

# Get all keys and sort them
sorted_keys = sorted(data.keys())

# Create new dictionary with sorted keys
sorted_dict = {}

for key in sorted_keys:
    sorted_dict[key] = data[key]   # Assign values according to sorted keys

# Display result
print("Sorted dictionary =", sorted_dict)