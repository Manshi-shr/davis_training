#to calculate final price after discount
#using function calculate the final price after discount
def calculate_discount(p, d):
    return p * (1 - d/100)
#taking input from the user
price = float(input("Enter the original price:"))
discount = float(input("Enter the discount percentage:"))
#displaying output
print("Final Price =", calculate_discount(price, discount))