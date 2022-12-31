n=int(input())
s=0
pr=1
while n>0:
    p=n%10
    pr=pr*p
    s=s+p
    n=n//10
print(pr-s)
