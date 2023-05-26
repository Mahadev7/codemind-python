n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    b=x.count(i)
    if b>c and b>n/2:
        c=i
print(c)