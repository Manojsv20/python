def lcm(a,b):
    if a>b:
        great=a
    else:
        great=b
    while(True):
        if(great%a==0 and great%b==0):
            return great
        great+=1
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(lcm(a,b))
