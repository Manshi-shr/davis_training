# Function to return all even numbers from a list

def get_even(numbers):
    
    # Initialize empty list
    even_list = []
    
    # Loop through list
    for num in numbers:
        
        # Check if number is even
        if num % 2 == 0:
            even_list.append(num)   # Add to list
    
    return even_list


# Taking input from user
# Example input: 1 2 3 4
nums = list(map(int, input("Enter the numbers: ").split()))

# Call function
result = get_even(nums)

# Display result
print("Even numbers =", result)