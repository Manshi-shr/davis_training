#to calculate final price after discount

# Taking input from user
price = float(input("Enter the original price: "))
discount = float(input("Enter discount percentage: "))

# Calculating discount amount
discount_amount = (price * discount) / 100

# Calculating final price
final_price = price - discount_amount

# Displaying result
print("Final price after discount is:", final_price)
















