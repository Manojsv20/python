def arm(n):
    a, b = n, n
    count=0
    while a>0 :
        count+=1
        a=a//10
    sum=0
    while(b>0):
        r=b%10
        sum=sum+pow(r,count)
        b=b//10
    if(n==sum):
        return 1
    else:
        return 0




n=int(input("Enter a str num :"))
e=int(input("enter the end value :"))
for i in range(n,e+1):
    if (arm(i)):
        print(i,end=" ")
   