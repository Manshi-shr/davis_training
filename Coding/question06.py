#to calculate the final price after discount

price = float(input("Enter the original price:"))
discount = float(input("Enter the discount percentage:"))
#calculating discount anf final pricce
discount_amount = (price * discount) / 100
final_price = price - discount_amount
#displaying output
print("Final Price =", final_price)