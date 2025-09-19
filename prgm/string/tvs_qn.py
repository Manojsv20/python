c=input("enter :")
a=int(input("count :"))
l=c.split()
s=0
# print(len(l))
for i in l:
    if(len(i)==a):
        print(i)
        s+=1
if(s==0):
    print("nothing")

