a=input()
a=a.lower()
s=[]
c=0
for i in a:
    if i!=' ':
        s.append(i)
s=set(s)
s=sorted(s)
#print(len(s))
for i in s:
    c+=1
print(c)