age = int(input("Enter age: "))

eligible_set = set(range(18, 150))

print("Eligible" if age in eligible_set else "Not Eligible")