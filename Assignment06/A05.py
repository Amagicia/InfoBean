age = int(input("Enter age: "))

if age < 12:
    price = 100
elif age <= 60:
    price = 200
else:
    price = 150

print("Ticket Price: ₹", price)