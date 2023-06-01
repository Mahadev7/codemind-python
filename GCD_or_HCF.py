a,b = map(int,input().split())
c = max(a,b)
l=[]
for i in range(1,c+1):
    if a%i==0 and b%i == 0:
        l.append(i)
print(max(l))