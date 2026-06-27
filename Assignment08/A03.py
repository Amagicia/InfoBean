amount = int(input("Enter Transaction Amount: "))

if amount >= 10000:
    location = input("Enter Location (international/domestic): ").lower()

    if location == "international":
        otp = input("OTP Verified? (yes/no): ").lower()

        if otp == "yes":
            print("Transaction Status = Allowed")
        else:
            print("Transaction Status = Blocked")

    else:
        if amount >= 50000:
            account_age = int(input("Enter Account Age (years): "))

            if account_age >= 2:
                print("Transaction Status = Allowed")
            else:
                print("Transaction Status = Flagged")
        else:
            print("Transaction Status = Allowed")

else:
    activity = input("Unusual Activity? (yes/no): ").lower()

    if activity == "yes":
        print("Transaction Status = Flagged")
    else:
        print("Transaction Status = Allowed")