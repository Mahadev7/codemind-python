a=input()
a=a.lower()
d={}
c=[]
cn=0
a1=[]
for i in a:
    if i.isalpha():
        a1.append(i)
for i in a1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if j==1:
        c.append(i)
        cn+=1
#print(len(c))
print(cn)