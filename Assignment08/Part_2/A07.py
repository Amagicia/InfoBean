marks = int(input("Enter Marks: "))

if marks >= 75:

    backlog = int(input("Enter Backlogs: "))

    if backlog == 0:

        project = int(input("Enter Project Score: "))

        if project >= 80:
            print("Result = First Class with Distinction")
        else:
            print("Result = First Class")

    else:
        print("Result = First Class")

elif marks >= 60:

    backlog = int(input("Enter Backlogs: "))

    if backlog <= 2:
        print("Result = Second Class")
    else:
        print("Result = Pass Class")

elif marks >= 50:
    print("Result = Pass")

else:
    print("Result = Fail")