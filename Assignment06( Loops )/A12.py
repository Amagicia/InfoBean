bill = int(input("Enter bill amount: "))

if bill <= 1000:
    gst = 0.05
elif bill <= 5000:
    gst = 0.12
else:
    gst = 0.18

final = bill + (bill * gst)

if bill > 3000:
    final += 200

print("Final Bill Amount: ₹", int(final))