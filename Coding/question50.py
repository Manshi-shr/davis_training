#to calculate si
class Interest:
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    @property
    def result(self):
        return (self.p * self.r * self.t) / 100

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

obj = Interest(p, r, t)

print("Simple Interest:", obj.result)