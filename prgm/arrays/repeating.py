
def repeat(a,l):
    my={}
    for i in range(l):
        if a[i] in my:
            my[a[i]]+=1
        else:
            my[a[i]]=1
    for i in my:
        if (my[i] > 1):
            print(i)


a=[10,20,30,40,50,10,20,20]
l=len(a)
repeat(a,l)