amount = int(input("Enter Order Amount: "))
customer = input("Enter Customer Type (VIP/Normal): ").lower()

if amount >= 2000:
    if customer == "vip":
        payment = input("Enter Payment Method (online/offline): ").lower()

        if payment == "online":
            print("Offer = Free Dessert + 20% Discount")
        else:
            print("Offer = Free Dessert")

    else:
        if amount >= 5000:
            print("Offer = 15% Discount")
        else:
            print("Offer = 10% Discount")

else:
    if amount >= 1000:
        if customer == "vip":
            print("Offer = 10% Discount")
        else:
            print("Offer = 5% Discount")
    else:
        print("Offer = No Offer")