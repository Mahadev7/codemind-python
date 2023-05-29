a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=[]
p=[]
for i in x:
    if i in y:
        z.append(i)
for i in y:
    if i in x:
        z.append(i)
for b,i in enumerate(z):
    if i not in z[:b]:
        p.append(i)
print(*p)
    