n = int(input())
x = list(map(int,input().split()))
k = int(input())
l = []
for i in x:
    if x.count(i)==k:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(*set(l))