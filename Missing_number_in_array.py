for i in range(int(input())):
    a=int(input())
    x=list(map(int,input().split()))
    c=[]
    p=[]
    for i in range(1,a+1):
        c.append(i)
    for i in c:
        if i not in x:
            p.append(i)
    print(*p)