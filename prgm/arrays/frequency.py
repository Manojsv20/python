def fre(a,n):
    my=dict()
    for i in range (n):
        if(a[i] in my.keys()):
            my[a[i]]+=1
        else:
            my[a[i]]=1
    for i in my:
        print(i," ",my[i])
a=[2,3,4,1,2,5,3,2,7,7,7,9]
n=len(a)
fre(a,n)
