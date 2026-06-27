moisture = int(input("Enter Soil Moisture: "))

if moisture <= 30:
    temperature = int(input("Enter Temperature: "))

    if temperature >= 35:
        crop = input("Enter Crop Type: ").lower()

        if crop == "wheat":
            print("Irrigation = High Water Supply")
        else:
            print("Irrigation = Moderate Water Supply")

    else:
        print("Irrigation = Moderate Water Supply")

elif moisture <= 60:
    rainfall = input("Rain Expected? (yes/no): ").lower()

    if rainfall == "yes":
        print("Irrigation = Delay Irrigation")
    else:
        print("Irrigation = Light Irrigation")

else:
    print("Irrigation = No Irrigation")