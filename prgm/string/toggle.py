def toggle(a,l):
    s=""
    for i in a:
        if(i.isupper()):
            i=i.lower()
        else:
            i=i.upper()
        s=s+i
    print(s)

a=input("Enter the character :")
l=len(a)
toggle(a,l)
print(a)