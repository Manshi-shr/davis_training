# Function to calculate total bill amount

def calculate_total(bill_list):
    
    # Initialize total
    total = 0
    
    # Loop through list and add each value
    for amount in bill_list:
        total += amount
    
    # Return total amount
    return total


# Taking input from user
# Example input: 100 200 300
bill = list(map(int, input("Enter bill amounts: ").split()))

# Call function and store result
result = calculate_total(bill)

# Display result
print("Total bill =", result)