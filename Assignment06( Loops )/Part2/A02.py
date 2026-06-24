marks = int(input("Marks: "))
entrance = int(input("Entrance Score: "))
cat = input("Category: ")

if marks >= 70:
    if entrance >= 80:
        if cat == "general":
            print("Admitted")
        else:
            print("Admitted with Scholarship")
    else:
        if marks >= 85:
            print("Management Quota")
        else:
            print("Rejected")
else:
    if cat != "general" and marks >= 60:
        if entrance >= 70:
            print("Waitlist")
        else:
            print("Rejected")
    else:
        print("Rejected")