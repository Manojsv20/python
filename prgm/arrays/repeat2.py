
def repeat(a,l):
    v=[False for i in range(l)]
    for i in range(l):
        if(v[i]==True):
            continue
        count=1
        for j in range(i+1,l):
            if(a[i]==a[j]):
                v[j]=True
                count+=1
        if count!=1:
            print(a[i])


a=[10,20,30,40,50,10,20,20]
l=len(a)
repeat(a,l)