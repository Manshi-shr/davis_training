# Program to print all even numbers from 1 to N

# Taking input from user
n = int(input("Enter value of N: "))

# Loop from 1 to N
for i in range(1, n + 1):
    
    # Check if number is even
    if i % 2 == 0:
        print(i, end=" ")   # Print in same line