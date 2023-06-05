n=int(input())
l=[]
x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in range(n):
    c=x[i]+y[i]
    l.append(c)
print(*l)