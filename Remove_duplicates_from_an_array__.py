n=int(input())
x=list(map(int,input().split()))
res = []
[res.append(x) for x in x  if x not in res]
for i in res:
    print(i,end=' ')