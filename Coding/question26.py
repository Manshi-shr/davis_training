#to calculate the final price after discount

price, discount = map(float, input("Enter price and discount: ").split())

final_price = price * (100 - discount) / 100
#displaying the final price
print("Final price:", final_price)