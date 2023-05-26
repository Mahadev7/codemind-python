n=input()
n=n.lower()
l=[]
d={}
s=[]
for i in n:
    if i.isalpha():
        l.append(i)
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
#print(d)
for i,j in d.items():
    if j==1:
        s.append(i)
p=sorted(s)
re="".join(p)
print(re)