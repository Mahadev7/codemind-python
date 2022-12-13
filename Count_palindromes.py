def palin(x):
    rev=0
    p=0
    while x>0:
        p=x%10
        rev=(rev*10)+p
        x=x//10
    return rev
a=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if i==palin(i):
        c+=1
print(c)