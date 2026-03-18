#to calculate simple interest
si = lambda p, r, t: (p * r * t) / 100
#taking input from the user
p = float(input("Enter the principal value: "))
r = float(input("Enter the rate value: "))
t = float(input("Enter the value of time: "))
#displaying output
print("Simple Interest:", si(p, r, t))