#to print even numbers between 1 to N
#taking input form the user
n = int(input("Enter a number:"))
#appying loop 
for i in range(2, n+1, 2):
    print(i, end=" ")