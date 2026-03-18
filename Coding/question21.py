#to calculate the final price after discount
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount: "))
#calculating price
price -= (price * discount / 100)
#displaying final price
print("Final price:", price)