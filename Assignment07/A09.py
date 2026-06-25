n=int(input("Enter The Number : "))
temp = 0

rev=0
ans=0

while n>0:
    rev=n%10
    if rev%2==0:
        ans+=1   
    n=n//10
    temp+=1
    
if temp==ans:
    print("All Even")
else:
    print("Not All Even")