a=input()
a=a.lower()
b=[]
for i in a:
    if i!=' ':
        b.append(i)
b=set(b)
b=sorted(b)
for i in b:
    print(i,end='')