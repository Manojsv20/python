# a = [10, 89, 9, 56, 4, 80, 8]
import math
a=[]
n=int(input("enter the no of elements:"))
for i in range(n):
    b=int(input("enter the number:"))
    a.append(b)
first=second=math.inf
print(first,second)
for i in range(n):
    if(a[i]<first):
        second=first
        first=a[i]
    elif(a[i]!=first and a[i]<second):
        second=a[i]
print(f"the second value is {second}")