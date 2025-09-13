# a = [10, 89, 9, 56, 4, 80, 8]
a=[]
n=int(input("enter the no of elements:"))
for i in range(n):
    b=int(input("enter the number:"))
    a.append(b)
max=a[0]
i=0
while(i<n):
    if(a[i]>max):
        max=a[i]
    i+=1
print(f"The largest number is {max}")
