r,c = map(int,input().split())
m = []
for i in range(r):
    x = list(map(int,input().split()))
    m.append(x)
s = 0
for i in range(r):
    for j in range(c):
        s+=m[i][j]
print(s)