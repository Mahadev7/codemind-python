for _ in range(int(input())):
    a = input()
    l,m = [],[]
    z = 0
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            l.append(a[i+1])
        else:
            m.append(z)
    if len(l)<=len(m):
        print(len(l))
    elif len(l)>len(m):
        print(len(l))
    else:
        print(0)