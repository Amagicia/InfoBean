stock = int(input("Enter Stock: "))
priority = input("Enter Priority (high/low): ").lower()

if stock >= 100:
    if priority == "high":
        distance = int(input("Enter Delivery Distance: "))
        if distance <= 200:
            print("Dispatch Status = Dispatch Immediately")
        else:
            print("Dispatch Status = Dispatch via Fast Courier")
    else:
        if stock >= 300:
            print("Dispatch Status = Bulk Dispatch")
        else:
            print("Dispatch Status = Normal Dispatch")

else:
    if stock >= 50:
        if priority == "high":
            print("Dispatch Status = Partially Dispatch")
        else:
            print("Dispatch Status = Hold")
    else:
        print("Dispatch Status = Out of Stock")