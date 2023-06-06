n=int(input())
p=[]
m=[]
for i in range(1,n+1):
    c=2**i
    p.append(c)
for i in p:
    s=abs(i-n)
    m.append(s)
print(min(m))