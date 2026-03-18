try:
    age = int(input("Enter age: "))
    assert age >= 0

    print("Eligible" if age >= 18 else "Not Eligible")

except:
    print("Invalid input")