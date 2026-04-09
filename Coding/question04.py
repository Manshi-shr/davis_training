#to print even numbers from 1 to N

# Taking input
N = int(input("Enter a number: "))

# Printing even numbers
print("Even numbers between 1 and", N, "are:")
#applying loop 
for i in range(1, N + 1):
    if i % 2 == 0:
        print(i, end=" ")