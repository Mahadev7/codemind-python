a=int(input())
b=[]
c=list(map(int,input().split()))
for i in range(a):
    for j in range(i,a):
        d=c[i:j+1]
        b.append(d)
x=[]
for i in b:
    p=sum(i)
    x.append(p)
print(max(x))