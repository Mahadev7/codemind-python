for i in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    p=[]
    while True:
        if len(x)==1:
            p.append(x[0])
            break
        else:
            p.append(x[-1])
            p.append(x[0])
            x.pop(-1)
            x.pop(0)
        if len(x)==0:
            break
    print(*p)