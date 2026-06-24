att = int(input("Enter attendance percentage: "))

if att >= 75:
    print("Eligible")
elif att >= 60:
    print("Eligible with warning")
else:
    print("Not Eligible")