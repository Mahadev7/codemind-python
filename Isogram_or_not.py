a=input()
b=[]
c=0
for i in a:
    if i.isalpha():
        b.append(i)
for i in b:
    if b.count(i)==1:
        c+=1
if c==len(b):
    print("True")
else:
    print("False")