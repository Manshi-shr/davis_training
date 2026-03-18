#to check the eligibility to vote or not
def is_eligible(age):
    return age >= 18
#taking input
age = int(input("Enter age: "))

if is_eligible(age):
    print("Eligible")
else:
    print("Not Eligible")