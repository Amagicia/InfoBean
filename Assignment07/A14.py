n1,n2=map(int,input("Enter The Number : ").split(','))

if n1<=n2:
    while n1<n2:
        print(n1,end=" → ")
        n1+=1
    print(n1)
elif n1>=n2:
    while n1>n2:
        print(n1,end=" → ")
        n1-=1
    print(n1)
else:
    print("Already on the same floor")
    
    
