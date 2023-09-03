n=int(input())
x=list(map(str,input().split()))
c=''.join(x)
d1=int(c)+1
l = [i for i in str(d1)]
p=[]
for i in l:
    p.append(int(i))
print(*p)