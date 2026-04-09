#to calculate the final price after discount
#calculate final price using funtion
def calculate_bill(price, discount):
    return price * (1 - discount / 100)
#taking input form the user
price = float(input("Enter  the original price: "))
discount = float(input("Enter the discount: "))
#displaying output
print("Final price:", calculate_bill(price, discount))