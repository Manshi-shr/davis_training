# Program to find intersection of two sets

# Taking input for first set
set1 = set(map(int, input("Enter elements of first set: ").split()))

# Taking input for second set
set2 = set(map(int, input("Enter elements of second set: ").split()))

# Find intersection using intersection() method
intersection_set = set1.intersection(set2)

# Display result
print("Intersection =", intersection_set)