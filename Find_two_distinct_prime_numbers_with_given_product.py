def prime(s):
    # if s<2:
    #     return False
    for i in range(2,s):
        if s%i==0:
            return False
    return True
a=int(input())
p=[]
for i in range(2,a):
    for j in range(2,a):
        if prime(i) and prime(j):
            if i*j==a:
                p.append(i)
                p.append(j)
if sum(p)==0:
    print("-1")
else:
    x=set(p)
    print(*x)