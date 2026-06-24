salary = int(input("Enter salary: "))
exp = int(input("Enter years of experience: "))

if exp > 10:
    bonus = 0.20
elif exp >= 5:
    bonus = 0.10
elif exp >= 2:
    bonus = 0.05
else:
    bonus = 0

print("Bonus Amount: ₹", int(salary * bonus))