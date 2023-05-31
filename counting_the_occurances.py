a=input()
a=a.lower()
b=[]
c=input()
c1=[]
for i in a:
    if i.isalpha():
        b.append(i)
for i in b:
    if i in c:
       c1.append(i)
if len(c1)==0:
    print("-1")
else:
    print(len(c1))