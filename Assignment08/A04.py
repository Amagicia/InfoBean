demand = int(input("Enter Demand: "))
time = input("Enter Time (peak/offpeak): ").lower()

if demand >= 80:
    if time == "peak":
        distance = int(input("Enter Distance: "))

        if distance >= 10:
            print("Fare Multiplier = 2x Fare")
        else:
            print("Fare Multiplier = 1.5x Fare")

    else:
        if demand >= 90:
            print("Fare Multiplier = 1.8x Fare")
        else:
            print("Fare Multiplier = 1.3x Fare")

else:
    if demand >= 50:
        if time == "peak":
            print("Fare Multiplier = 1.2x Fare")
        else:
            print("Fare Multiplier = Normal Fare")
    else:
        print("Fare Multiplier = Normal Fare")