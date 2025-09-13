a=[10,20,3,4,5,7]
n=len(a)
for i in range(n//2):
    a[i],a[n-i-1]=a[n-i-1],a[i]
print(a)
print(a[::-1])