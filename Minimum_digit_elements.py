n=int(input())
x=list(map(str,input().split()))
c=0
a=[]
for i in x:
    l=len(i)
    a.append(l)
b=min(a)
for i in x:
    if len(i)==b:
        c+=1
print(c)