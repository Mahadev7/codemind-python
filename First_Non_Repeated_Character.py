for  i in range(int(input())):
    n=int(input())
    a=input()
    for i in range(n):
        if a.count(a[i])==1:
            print(a[i])
            break
    else:
        print(-1)