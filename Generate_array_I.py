n=int(input())
x=list(map(int,input().split()))
l=[]
for i in range(0,n,2):
    a=x[i]
    b=x[i+1]
    for i in range(b):
        l.append(a)
print(*l)