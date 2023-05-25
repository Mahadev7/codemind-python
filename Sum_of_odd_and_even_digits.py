n=int(input())
x=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if i%2==0:
        es+=x[i]
    else:
        os+=x[i]
if (es-os) == 0:
    print("YES")
else:
    print("NO")