def isdigit(n):
    s=0
    while n:
        p=n%10
        s+=p
        n=n//10
    return s
n=int(input())
p=len(str(n))
while n>9:
    n=isdigit(n)
print(n)