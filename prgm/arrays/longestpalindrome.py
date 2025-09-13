def ispalindrome(n):
    div=1
    while(int(n/div)>=10):
        div*=10
    while(n!=0):
        tail=int(n/div)
        head=int(n%10)
        if(head!=tail):
            return False
        n=int(n%div)/10
        div=int(div/100)
        return True
def longestpalindrome(a,l):
    mx=-1
    for i in range(l):
        if(a[i]>mx) and (ispalindrome(a[i])):
            mx=a[i]
    return mx
a= [1, 232, 5545455, 909090,1234567654321, 161]
l=len(a)
print(longestpalindrome(a,l))