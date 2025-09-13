from collections import Counter
a=[2,3,2,3,1,4,5,3,3,2,1,4,4]
my=Counter(a)
f=my.most_common()
for  x,y in f:
    print(x,y)
    