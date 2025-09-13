def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
a=int(input("enter no 1:"))
b=int(input("enter no 2:"))
print(gcd(a,b))
