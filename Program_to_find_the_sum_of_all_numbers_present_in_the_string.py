a=input()
s=0
b=[]
for i in a:
    if i.isdigit():
        b.append(i)
for i in b:
    s+=int(i)
print(s)