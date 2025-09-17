def rv(s):
    v="AEIOUaeiou"
    c=""
    for i in s:
        if i not in v:
            c=c+i
    return c

s=input("Enter:")
print(rv(s))