n=int(input("Enter The Number : "))


rev=0
ans=0

while n>0:
    rev=n%10
    if rev%2==0:
        ans+=1   
    n=n//10
    

print("Even Digits Count",ans)