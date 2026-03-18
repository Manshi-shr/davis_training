#to check the eligibility to vote or not
#using function check the eligiblity
def check(age):
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")
#taking input
age = int(input("Enter the age:"))
check(age)