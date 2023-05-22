n=int(input())
x=list(map(int,input().split()))
k=int(input())
s=[]
a=0
for i in x:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        s.append(i)
for i in s:
    if i<=k:
        a+=1
print(a)