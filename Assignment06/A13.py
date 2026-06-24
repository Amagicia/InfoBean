salary = int(input("Enter Salary : "))
rate = int(input("Enter rating : "))

hike=0

if rate==5:
    hike=salary*0.25
    if salary<20000:
        hike=hike+2000
    
elif rate==4:
    hike=salary*0.20
    if salary<20000:
        hike=hike+2000
        
elif rate==3:
    hike=salary*0.1
elif rate==2:
    hike=salary*0.05
else:
    hike=0



print("Revised Salary : ",int(hike+salary))

