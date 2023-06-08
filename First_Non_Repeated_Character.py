for i in range(int(input())):
    a=int(input())
    l=input()
    for i in range(a):
        if l.count(l[i])==1:
            print(l[i])
            break
    else:
        print('-1')