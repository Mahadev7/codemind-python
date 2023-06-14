n=int(input())
x=list(map(int,input().split()))
d={}
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    print(i,j,end=' ')