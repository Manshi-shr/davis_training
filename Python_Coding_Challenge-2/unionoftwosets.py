# Program to find union of two sets

# Taking input for first set
set1 = set(map(int, input("Enter elements of first set: ").split()))

# Taking input for second set
set2 = set(map(int, input("Enter elements of second set: ").split()))

# Find union using union() method
union_set = set1.union(set2)

# Display result
print("Union =", union_set)