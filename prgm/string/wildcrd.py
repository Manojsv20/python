def remvewild(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 != l2:
        return False
    wildcard="!@#$%^&*()?/"
    cl1=""
    cl2=""
    for i in range(len(s1)):
        if s2[i] not in wildcard:
            cl2+=s2[i]
            cl1+=s1[i]
    return cl1==cl2


s1=input("enter:")
s2=input("enter:")
print(remvewild(s1,s2))