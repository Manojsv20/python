def count(a,l):
    v=[False for i in range(l)]
    c=0
    for i in range(l):
        if(v[i]==True):
            continue
        for j in range(i+1,l):
            if(a[i]==a[j]):
                v[j]=True
        c+=1
    print(c)


a = [10, 30, 40, 20, 10, 20, 50, 10]
l=len(a)
count(a,l)