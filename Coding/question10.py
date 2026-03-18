#to calculate simple interest 
def simple_interest(p, r, t):
    return (p * r * t) / 100
#taking input form the user
p = float(input("Enter principal value:"))
r = float(input("Enter the rate value:"))
t = float(input("Enter the time:"))
#displaying output
print("Simple Interest =", simple_interest(p, r, t))