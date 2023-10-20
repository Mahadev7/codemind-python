for _ in range(int(input())):
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    p = k%n
    a = x[:-1*p]
    b = x[-1*p:]
    print(*(b+a))