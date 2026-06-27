income = int(input("Enter Income: "))
credit_score = int(input("Enter Credit Score: "))
employment = input("Enter Employment (government/private): ").lower()
debt = int(input("Enter Existing Debt: "))

if income >= 50000:
    if credit_score >= 750:
        if debt < 20000:
            print("Card Type = Premium Card")
        else:
            print("Card Type = Gold Card")
    else:
        if employment == "government" and credit_score >= 650:
            print("Card Type = Gold Card")
        else:
            print("Application Rejected")
else:
    if income >= 30000 and credit_score >= 700:
        print("Card Type = Silver Card")
    else:
        print("Application Rejected")