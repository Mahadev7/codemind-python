def Index(n,x):
    p,q = sum(x),0
    for i in range(n):
        q+=x[i]
        if p == q:
            return i
        p-=x[i]
    return -1
for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    print(Index(n,x))