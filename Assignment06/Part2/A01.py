age = int(input("Policy Age: "))
amount = int(input("Claim Amount: "))
acc = input("Accident Type: ")

if age >= 2:
    if amount <= 50000:
        if acc == "minor":
            print("Approved")
        else:
            print("Approved with Inspection")
    elif amount <= 200000:
        if acc == "major":
            print("Approved with Investigation")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    if acc == "minor":
        print("Rejected")
    else:
        print("Pending Review")