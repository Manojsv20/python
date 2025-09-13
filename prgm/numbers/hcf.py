def hcf(a,b):
    r=1
    for i in range(1,a+1):
        if(a%i==0) and (b%i==0):
            r=i
    return r
a=int(input("enter a number : "))
b=int(input("enter a number : "))
if b<a:
    a,b=b,a
print(hcf(a,b))