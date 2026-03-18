#to check the eligibility to vote or not
def check_vote(age):
    return "Eligible" if age >= 18 else "Not Eligible"

age = int(input("Enter age: "))

print(check_vote(age))
