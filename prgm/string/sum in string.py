def som(c):
    num="1234567890" #48-57 ASCII
    total=0
    for i in c:
        if i in num:
            total+=int(i)
    print(total)

c=input("enter:")
som(c)