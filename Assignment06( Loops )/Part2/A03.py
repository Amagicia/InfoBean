salary = int(input("Salary: "))
score = int(input("Credit Score: "))
loans = int(input("Existing Loans: "))

if salary >= 30000:
    if score >= 750:
        if loans == 0:
            print("Low Risk")
        elif loans <= 2:
            print("Medium Risk")
        else:
            print("High Risk")
    else:
        if salary >= 50000 and score >= 650:
            print("Medium Risk")
        else:
            print("High Risk")
else:
    print("Not Eligible")
    