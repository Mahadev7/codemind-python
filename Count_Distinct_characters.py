a=input()
a=a.lower()
b=[]
c=0
for i in a:
    if i!=' ':
        b.append(i)
b=set(b)
b=sorted(b)
print(len(b))