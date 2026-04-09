#to calculate the final price after discount
print("Final price:",
      (lambda p, d: p - (p*d/100))(
          float(input("Enter the original  price: ")),
          float(input("Enter the discount: "))
      ))