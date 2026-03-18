#to print all the even numbers between 1 to N
#taking input from the user
N = int(input("Enter any number: "))

even_numbers = [i for i in range(1, N+1) if i % 2 == 0]
#displaying output
print("Even numbers:", even_numbers)