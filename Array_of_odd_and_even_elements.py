n=int(input())
x=list(map(int,input().split()))
e=[]
o=[]
for i in x:
    if i%2==0:
        e.append(i)
for i in x:
    if i%2!=0:
        o.append(i)
print(*o,*e)