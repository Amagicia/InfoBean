travel_class = input("Enter Class (business/economy): ").lower()
distance = int(input("Enter Distance: "))

if travel_class == "business":
    if distance > 1000:
        print("Ticket Price = 8000")
    else:
        print("Ticket Price = 5000")

elif travel_class == "economy":
    if distance > 1000:
        booking = input("Booking Time (early/late): ").lower()

        if booking == "early":
            print("Ticket Price = 4000")
        else:
            print("Ticket Price = 5000")
    else:
        print("Ticket Price = 2500")