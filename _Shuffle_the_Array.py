n = int(input())
x = list(map(int,input().split()))
k = int(input())
p = x[:k]
q = x[k:]
l = []
for i in range(len(p)):
    l.append(p[i])
    l.append(q[i])
print(*l)