a=int(input())
y=list(map(int,input().split()))
p=0
for i in range(a):
    if y[i]%2==1:
        p+=1
if p>2:
    print("NO")
else:
    print("YES")