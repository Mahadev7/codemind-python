n=int(input())
x=list(map(int,input().split()))
k=int(input())
a=[]
p=0
for i in x:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        a.append(i)
for i in a:
    if i>=k:
        p+=1
print(p)