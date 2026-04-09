# Program to calculate total weekly sales

# Taking list input from user
# Example input: 100 200 150 300 250 400 100
sales = list(map(int, input("Enter 7 days sales separated by space: ").split()))

# Initialize total to 0
total = 0

# Loop through each day's sale and add to total
for i in sales:
    total = total + i

# Display total sales
print("Total weekly sales =", total)