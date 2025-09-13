n=int(input("enter"))
s=n*n
print(n,s,end="\n")
while(n>0):
    if(n%10==s%10):
        n=n//10
        s=s//10
        pass
    else:
        break

if(n<=0):
    print("its ok")
else:
    print("nah")