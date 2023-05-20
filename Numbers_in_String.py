a=input()
s=[]
r=0
for i in a:
    if i.isdigit():
        s.append(i)
for i in s:
    r+=int(i)
print(r)