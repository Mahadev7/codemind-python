n=int(input())
x=list(map(int,input().split()))
a=[]
for i in x:
    if i==x.count(i):
        a.append(i)
b=set(a)
print(len(b))