n=int(input())
x=list(map(int,input().split()))
a=[]
s=0
for i in x:
    if i>s:
        a.append(i)
        s=i
if a==x:
    print("yes")
else:
    print("no")