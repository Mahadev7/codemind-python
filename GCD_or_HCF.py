def lcm(m,n):
    t=2
    res=1
    while m>=t and n>=t:
        if m%t==0 and n%t==0:
            m=m//t
            n=n//t
            res=res*t
           # return res
        else:
            t+=1
    return res



m,n=map(int,input().split())
print(lcm(m,n))