#to print all the even numbers between 1 to N
N = int(input("Enter N: "))

even_numbers = [i for i in range(1, N+1) if (i & 1) == 0]

print("Even numbers:", even_numbers)