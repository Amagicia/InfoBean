num=int(input("Enter The Number : "))


sum=1

while num>0:
    rev=num%10
    
    sum*=rev
    num//=10
    
if sum%2==0:
    print("Even")
else:
    print("Odd")
