vehicle=input("Enter Vehicle type : ")
hours=int(input("Enter hours parked : "))

money=0

if vehicle.lower()=="bike":
    money=10*hours
elif vehicle.lower()=="car":
    money=20*hours
else:
    money=50*hours

if hours>=5:
    money +=100
    
print("Total Parking Fee:  ₹",money)