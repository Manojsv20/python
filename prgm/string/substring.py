def rep(c,new,old):
    result=""
    i=0
    while(i<len(c)):
        if(c[i:i+len(old)]==old):
            result+=new
            i+=len(old)
        else:
            result+=c[i]
            i+=1
    return result

c=input("string:")
new=input("new:")
old=input("old:")
print(rep(c,new,old))