def chk(c):
    s=""
    for i in c:
        if('a'<=i<='z' or 'A'<=i<='Z'):
            s=s+i
    return s
def pal(s):
    b=s[::-1]
    if(s==b):
        return "palindrome"
    else:
        return "not"


c=input("Enter:")
s=chk(c)
print(s)
print(pal(s))