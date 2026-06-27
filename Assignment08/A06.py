experience = int(input("Enter Experience (years): "))
rating = int(input("Enter Rating: "))

if experience >= 5:
    if rating >= 4:
        projects = int(input("Enter Projects Completed: "))

        if projects >= 3:
            salary = int(input("Enter Salary: "))

            if salary <= 50000:
                print("Promotion Status = Promoted with 30% Hike")
            else:
                print("Promotion Status = Promoted with 20% Hike")

        else:
            print("Promotion Status = Promoted with 10% Hike")

    else:
        print("Promotion Status = No Promotion")

else:
    if rating == 5:
        print("Promotion Status = Fast Track Promotion")
    else:
        print("Promotion Status = No Promotion")