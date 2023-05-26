def prime(i):
    if i<2:
        return False
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return 0
    return 1
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if prime(i) and i!=0:
        c+=1
print(c)