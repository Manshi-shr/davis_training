#to print all he even numbers bt 1 to N
N = int(input("Enter any number: "))

even_numbers = list(map(lambda x: x*2, range(1, N//2 + 1)))

print("Even numbers:", even_numbers)