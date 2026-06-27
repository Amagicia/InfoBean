amount = int(input("Enter Transaction Amount: "))
location = input("Enter Location (international/domestic): ").lower()

if amount >= 50000:

    if location == "international":

        device = input("Enter Device (new/old): ").lower()

        if device == "new":

            transactions = int(input("Enter Transaction Count: "))

            if transactions > 3:
                print("Risk Level = High Risk (Blocked)")
            else:
                print("Risk Level = Medium Risk")

        else:
            print("Risk Level = Medium Risk")

    elif location == "domestic":

        transactions = int(input("Enter Transaction Count: "))

        if transactions > 5:
            print("Risk Level = Medium Risk")
        else:
            print("Risk Level = Low Risk")

else:

    activity = input("Unusual Activity? (yes/no): ").lower()

    if activity == "yes":

        device = input("Enter Device (new/old): ").lower()

        if device == "new":
            print("Risk Level = Medium Risk")
        else:
            print("Risk Level = Low Risk")

    else:
        print("Risk Level = Safe")