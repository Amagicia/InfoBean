n=int(input("Enter The Number : "))

rev=0
ans=0

while n>0:
    rev=n%10
    ans=rev+ans*10    
    n=n//10
    
# for i in range(0,len(str(n))):
#     rev=n%10
#     ans=rev+ans*10    
#     n=n//10
    
print(ans)