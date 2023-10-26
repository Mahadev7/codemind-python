n = int(input())
x = list(map(int,input().split()))
s = []
for i in range(0,n,2):
    p = x[i]
    q = x[i+1]
    for i in range(p):
        s.append(q)
print(*s)