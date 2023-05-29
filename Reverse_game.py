n=int(input())
x=list(map(str,input().split()))
s=[]
for i in x:
    j=i[::-1]
    s.append(int(j))
print(*s)