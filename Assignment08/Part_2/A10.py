age = int(input("Enter Age: "))

if 18 <= age <= 25:

    bmi = float(input("Enter BMI: "))

    if 18 <= bmi <= 25:

        running = float(input("Enter Running Time (minutes): "))

        if running <= 15:

            medical = input("Medical Status (fit/unfit): ").lower()

            if medical == "fit":
                print("Selection Status = Selected")
            else:
                print("Selection Status = Medical Reject")

        else:
            print("Selection Status = Physical Fail")

    else:
        print("Selection Status = BMI Fail")

elif 26 <= age <= 30:

    running = float(input("Enter Running Time (minutes): "))
    medical = input("Medical Status (fit/unfit): ").lower()

    if running <= 14 and medical == "fit":
        print("Selection Status = Conditional Selection")
    else:
        print("Selection Status = Rejected")

else:
    print("Selection Status = Not Eligible")