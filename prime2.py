k=int(input("enter start:"))
l=int(input("enter stop:"))
for n in range(k,l):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if count==2:
        print("number is prime",n)
                   
