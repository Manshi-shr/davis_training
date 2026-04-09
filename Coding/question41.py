#to calculte the final price after discount
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

final_price = price * (100 - discount) / 100

print("Final price after discount is: {:.2f}".format(final_price))