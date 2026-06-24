amount = int(input("Enter purchase amount: "))

if amount > 5000:
    discount = 0.20
elif amount >= 2000:
    discount = 0.10
else:
    discount = 0.05

final = amount - (amount * discount)
print("Final Amount: ₹", int(final))