def cv(s):
    v="AEIOUaeiou"
    count=0
    for i in s:
        if i in v:
            count+=1
    return count

s=input("Enter:")
print(cv(s))