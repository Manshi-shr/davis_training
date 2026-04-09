# Function to calculate Simple Interest

def simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI

# Taking input
P = float(input("Enter the value of Principal : "))
R = float(input("Enter the value of Rate : "))
T = float(input("Enter the value of Time : "))

# Function call
result = simple_interest(P, R, T)

# Output
print("Simple Interest is:", result)