num=int(input("Enter The Number : "))
digit=int(input("Enter The Digit : "))


sum=0
while num>0:
    rev=num%10
    
    if rev==digit:
        sum+=1
    num//=10
    
print(sum)
