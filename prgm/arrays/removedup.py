def dup(a,l):
    j=0
    temp=list(range(l))
    for i in range(l-1):
        if(a[i]!=a[i+1]):
            temp[j]=a[i]
            j+=1
    temp[j]=a[l-1]
    j+=1

    for i in range(j):
        a[i]=temp[i]
    return a

a=[10,10,20,20,20,90]
l=len(a)
dup(a,l)

