def calculatesi(p,r,t):
    return ((p*r*t)/100)
principal=float(input("Enter the principal(in Rs):"))
rate =float(input("Enter the rate(in Rs):"))
time=int(input("Enter the time(in yrs):"))
print("Simple interest: Rs", calculatesi(principal,rate,time)) 