# Program to assign grade based on marks

# Taking input from user
marks = int(input("Enter marks: "))

# Assigning grades using conditions
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("D")   # Below 50