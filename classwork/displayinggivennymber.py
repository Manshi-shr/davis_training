num = int(input("Enter a number: "))

print("Even factors are:")

for i in range(1, num + 1):
    if num % i == 0 and i % 2 == 0:
        print(i)