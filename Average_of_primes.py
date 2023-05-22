n=int(input())
x=list(map(int,input().split()))
s=[]
for i in x:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        s.append(i)
l=len(s)
a=sum(s)/l
print("%.2f" %a)