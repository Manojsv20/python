def fibo(n):
    a,b=0,1
    fi=[]
    if(n>=1):
        fi.append(a)
    if(n>=2):
        fi.append(b)
    for i in range(2,n):
        next=a+b
        fi.append(next)
        a,b=b,next
    return fi
n= int(input("enter"))
print(fibo(n))
print(*(x for x in fibo(n)))