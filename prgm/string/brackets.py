def reexp(c):
    exp="(){}[]"
    for i in c:
        if i in exp:
            continue
        else:
            print(i,end='')

c=input("enter the expression :")
reexp(c)