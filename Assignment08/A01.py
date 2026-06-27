subscription = input("Enter Subscription (premium/basic): ").lower()
progress = int(input("Enter Course Progress: "))

if subscription == "premium":
    if progress >= 80:
        score = int(input("Enter Test Score: "))
        if score >= 70:
            print("Access Status = Certificate Unlocked")
        else:
            print("Access Status = Retry Test")
    else:
        print("Access Status = Complete the Course")

elif subscription == "basic":
    if progress >= 50:
        print("Access Status = Limited Access")
    else:
        print("Access Status = Content Locked")

else:
    print("Access Status = Access Denied")