price, discount = map(float, input("Enter price and discount: ").split())

final_price = price * (100 - discount) / 100

print("Final price:", final_price)