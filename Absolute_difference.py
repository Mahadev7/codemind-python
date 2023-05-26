# 1 id discarded
def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
x=list(map(int,input().split()))
p=1
np=1
for i in x:
    if prime(i):
        p*=i
    else:
        np*=i
print(abs(p-np))
