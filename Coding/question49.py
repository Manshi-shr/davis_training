#to print all the even numbers between 1 to N
def even_gen(n):
    for i in range(2, n+1, 2):
        yield i

N = int(input("Enter N: "))

print("Even numbers:", list(even_gen(N)))