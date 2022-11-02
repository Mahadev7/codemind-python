n=int(input())
x=list(map(int,input().split()))
z=int(input())
cnt=0
for i in x:
    if i==z:
        cnt+=1
print(cnt)