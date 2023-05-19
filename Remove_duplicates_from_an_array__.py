n=int(input())
m=list(map(int,input().split()))
p=[]
for i in m:
    if i not in p:
        p.append(i)
for i in p:
    print(i,end=' ')