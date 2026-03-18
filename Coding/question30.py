def simple_interest(*args):
    p, r, t = args
    return (p * r * t) / 100

values = list(map(float, input("Enter P R T: ").split()))
print("Simple Interest:", simple_interest(*values))