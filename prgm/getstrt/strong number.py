def fact(n):
    if(n<=1):
        return 1
    else:
        return n * fact(n-1)


def strong(n):
    a=n
    sum=0
    while(a>0):
        r=a%10
        sum=sum+fact(r)
        a=a//10
    if sum==n:
        return 1
    else:
        return 0

n=int(input("enter a number"))
if (strong(n)):
    print(f"the {n} is strong ")
else:
    print("nope")