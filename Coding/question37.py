age = int(input("Enter age: "))
#find eligibility to vote
match age >= 18:
    case True:
        print("Eligible")
    case False:
        print("Not Eligible")