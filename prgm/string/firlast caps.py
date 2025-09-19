def firlast(c):
    n=len(c)
    for i in range(n):
        if(i==0 or i==n-1):
            print(c[i].upper(),end='')
        else:
            print(c[i],end='')

c=input("enter")
firlast(c)