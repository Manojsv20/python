def prime(n):
    count=0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if(count==0):
        return n

def factor(n):
    for i in range(2,n):
        if(n%i==0) and prime(i):
            print(i,end=" ")
    #print(n)

n=int(input("enter"))
factor(n)
