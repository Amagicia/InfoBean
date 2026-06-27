salary = int(input("Enter Salary: "))
credit_score = int(input("Enter Credit Score: "))

if salary >= 40000:

    age = int(input("Enter Age: "))

    if 21 <= age <= 60:

        if credit_score >= 750:

            emi = int(input("Enter EMI: "))

            if emi <= salary * 0.40:
                print("Loan Status = Approved at 8%")
            else:
                print("Loan Status = Approved at 10%")

        elif credit_score >= 650:
            print("Loan Status = Approved at 12%")

        else:
            print("Loan Status = Rejected")

    else:
        print("Loan Status = Rejected")

else:

    if salary >= 25000 and credit_score >= 700:
        print("Loan Status = Approved at 13%")
    else:
        print("Loan Status = Rejected")