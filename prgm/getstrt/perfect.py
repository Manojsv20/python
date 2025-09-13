def per(n):
    lst=[]
    f=0
    for i in range(1,n):
        if(n%i==0):
            f=f+i
            lst.append(i)
    if(f==n):
        print(lst)
        return 1
    else:
        return 0

n=int(input("enter to chk"))
if per(n):
    print("perfect")
else:
    print("no, its not")