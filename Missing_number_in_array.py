for _ in range(int(input())):
    n=int(input())
    a = list(map(int,input().split()))
    p = n*(n+1)//2
    s=sum(a)
    print(abs(p-s))