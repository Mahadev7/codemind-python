for _ in range(int(input())):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    p=a+b
    m=sorted(p)
    print(*m)