x=list(map(str,input().split()))
s=0
for i in x:
    i=i.lower()
    if i==i[::-1]:
        s+=1
print(s)