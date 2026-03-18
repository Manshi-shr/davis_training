#to calculate si
def calculate():
    def si(p, r, t):
        return (p * r * t) / 100

    p = float(input("Enter P: "))
    r = float(input("Enter R: "))
    t = float(input("Enter T: "))

    print("Simple Interest:", si(p, r, t))

calculate()