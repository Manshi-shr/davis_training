# Age Classification Program
#taking input from user
age = int(input("Enter your age: "))
#check conditions on categories whether the age under minor, adult or senior
if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")