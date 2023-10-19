n = int(input())
m1,m2 = [],[]
for i in range(n):
    x = list(map(int,input().split()))
    m1.append(x)
for i in range(n):
    y = list(map(int,input().split()))
    m2.append(y)
m = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        m[i][j] = abs(m1[i][j]-m2[i][j])
for i in m:
    print(*i)