n=int(input("Enter The Number : "))
temp = n
rev=0
ans=0

while n>0:
    rev=n%10
    ans=rev+ans*10    
    n=n//10
    
if temp == ans:
    print("Palindrome")
else:
    print("Not Palindrome")