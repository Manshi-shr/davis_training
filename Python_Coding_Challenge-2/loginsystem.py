# Login Validation
#taking login credentials from the user
username = input("Enter the  username: ")
password = input("Enter the password: ")

# Correct credentials
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")