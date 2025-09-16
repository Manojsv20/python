
def dis(a,l):
    my=dict()
    for i in range(l):
        if a[i] in my.keys():
            my[a[i]]+=1
        else:
            my[a[i]]=1
    for i in my:
        if(my[i]==1):
            print(i);


a=[10,20,3,10,20,3,400]
l=len(a)
dis(a,l)