N = int(input("Enter N: "))

nums = list(range(1, N+1))
even_numbers = list(filter(lambda x: x % 2 == 0, nums))

print("Even numbers:", even_numbers)