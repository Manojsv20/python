def sot(a,n):
    for i in range (n-1):
        flag = 0
        for j in range(n-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                flag=1
        if(flag==0):
                break
    return a


a=[2,2,4,5,11,29,445]
n=len(a)
print(sot(a,n))