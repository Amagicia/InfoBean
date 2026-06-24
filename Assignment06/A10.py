data = float(input("Enter daily data usage: "))

if data > 3:
    print("Premium Plan")
elif data >= 1:
    print("Standard Plan")
else:
    print("Basic Plan")