#to calculate the si using static method
class SI:
    @staticmethod
    def calculate(p, r, t):
        return (p * r * t) / 100

p = float(input("Enter thr value of principal: "))
r = float(input("Enter the value of rate: "))
t = float(input("Enter the value of time: "))
#displayiny output
print("Simple Interest:", SI.calculate(p, r, t))