data = {
    "price": float(input("Enter price: ")),
    "discount": float(input("Enter discount: "))
}

final = data["price"] - (data["price"] * data["discount"] / 100)

print("Final price:", final)