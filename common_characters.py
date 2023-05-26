a=input()
b=input()
a=a.lower()
b=b.lower()
l,n=[],[]
sh=[]
for i in a:
    if i.isalpha():
        l.append(i)
for i in b:
    if i.isalpha():
        n.append(i)
p=set(l)
q=set(n)
for i in p:
    if i  in q:
        sh.append(i)
sa=sorted(sh)
if len(sh)==0:
    print('-1')
else:
    for i in sa:
        print(i,end='')
        