dist = int(input("Enter distance: "))
cls = input("Enter class: ")

if dist <= 100:
    fare = 100 if cls == "Sleeper" else 200
elif dist <= 500:
    fare = 300 if cls == "Sleeper" else 600
else:
    fare = 500 if cls == "Sleeper" else 1000

print("Total Fare: ₹", fare)