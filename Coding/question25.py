#calculating si
def simple_interest(p=0, r=0, t=0):
    return (p * r * t) / 100

p = float(input("Enter the value of principal: "))
r = float(input("Enter the value of rate: "))
t = float(input("Enter the value of time: "))
#displaying si
print("Simple Interest:", simple_interest(p, r, t))