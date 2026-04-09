# Program to determine ticket price based on day

# Taking input from user
day = input("Enter day: ")

# Convert input to lowercase for easy comparison
day = day.lower()

# Checking day and assigning price
if day == "sunday":
    print(200)   # Ticket price for Sunday
elif day == "saturday":
    print(180)   # Ticket price for Saturday
else:
    print(150)   # Ticket price for other days