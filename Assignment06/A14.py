category = input("Enter course category : ")
user = input("Enter user type : ")

money=0
discount =0

if category.lower()=="programming":
    money=5000
elif category.lower()=="design":
    money=4000
elif category.lower()=="marketing":
    money=3000


if user.lower()=="student":
    discount=(20*money)/100
elif user.lower()=="working professional":
    discount=(10*money)/100
else :
    discount=0

print("Final Course Fee: ₹",int(money-discount))

