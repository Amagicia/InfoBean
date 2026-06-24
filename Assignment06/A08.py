temp = int(input("Enter temperature: "))

if temp < 0:
    print("Freezing")
elif temp <= 20:
    print("Cold")
elif temp <= 35:
    print("Warm")
else:
    print("Hot")