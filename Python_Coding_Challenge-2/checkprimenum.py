# Function to check whether a number is prime

def is_prime(num):
    
    # Prime numbers are greater than 1
    if num <= 1:
        return False
    
    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            return False   # Not prime if divisible
    
    return True   # Prime if no divisors found


# Taking input from user
n = int(input("Enter a number: "))

# Call function and print result
if is_prime(n):
    print("Prime")
else:
    print("Not Prime")