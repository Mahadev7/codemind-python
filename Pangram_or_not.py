a=input()
a=a.lower()
b=[]
c='abcdefghijklmnopqrstuvwxyz'
for i in a:
    if i!=' ':
        b.append(i)
b=set(b)
if len(b)==len(c):
    print("True")
else:
    print("False")