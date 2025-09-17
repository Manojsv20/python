
def rotate(a,n):
    l = len(a)
    n=n%l
    print(n)
    b=[]
    for i in range(n,l):
        b.append(a[i])
    i=0
    while(i<n):
        b.append(a[i])
        i+=1
    for i in range(l):
        print(b[i],end=" ")
    print(b)



a=[10,20,30,40,50,60,70]
n=int (input("enter"))
rotate(a,n)