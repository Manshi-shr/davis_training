#to calculate the si using class 

class Interest:
    def calculate(self, p, r, t):
        return (p * r * t) / 100

obj = Interest()
#taking input form the user
p = float(input("Enter the  value of principal: "))
r = float(input("Enter the value of: "))
t = float(input("Enter the valur of time: "))
#displaying si
print("Simple Interest:", obj.calculate(p, r, t))