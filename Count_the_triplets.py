for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if a[i]+a[j]==a[k] or a[i]+a[k]==a[j] or a[j]+a[k]==a[i]:
                    c+=1
    if c == 0:
        print(-1)
    else:
        print(c)