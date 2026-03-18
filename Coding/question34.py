#to print all the even numbers bt 1 to N
def print_even(n):
    if n < 2:
        return
    print_even(n-2)
    print(n, end=" ")

N = int(input("Enter the number: "))
print_even(N if N % 2 == 0 else N-1)