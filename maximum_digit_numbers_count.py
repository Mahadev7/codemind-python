n=int(input())
x=list(map(str,input().split()))
l=0
a=[]
for i in x:
    l=len(i)
    a.append(l)
b=max(a)
for i in x:
    if len(i)==b:
        print(i,end=' ')