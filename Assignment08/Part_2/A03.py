marks = int(input("Enter Marks: "))
income = int(input("Enter Family Income: "))
category = input("Enter Category: ").lower()

if marks >= 85:
    if income <= 300000:
        if category != "general":
            print("Scholarship = Full Scholarship")
        else:
            print("Scholarship = 75% Scholarship")
    else:
        print("Scholarship = 50% Scholarship")

elif marks >= 70:
    if income <= 200000:
        print("Scholarship = 50% Scholarship")
    else:
        print("Scholarship = 25% Scholarship")

else:
    print("Scholarship = No Scholarship")