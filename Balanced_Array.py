def Balance(n,arr):
    p,q = sum(arr),0
    for i in range(n):
        q+=arr[i]
        if p == q:
            return "YES"
        p-=arr[i]
    return "NO"
for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    print(Balance(n,x))