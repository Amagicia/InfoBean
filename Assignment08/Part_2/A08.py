demand = int(input("Enter Demand: "))

if demand >= 80:

    stock = int(input("Enter Stock: "))

    if stock < 50:

        user = input("Enter User Type (premium/normal): ").lower()

        if user == "premium":

            festival = input("Festival? (yes/no): ").lower()

            if festival == "yes":
                print("Discount = 20%")
            else:
                print("Discount = 10%")

        else:
            print("Discount = No Discount")

    else:
        print("Discount = 5%")

elif demand >= 40:

    festival = input("Festival? (yes/no): ").lower()

    if festival == "yes":
        print("Discount = 10%")
    else:
        print("Discount = No Discount")

else:

    stock = int(input("Enter Stock: "))

    if stock > 200:
        print("Discount = 15%")
    else:
        print("Discount = No Discount")