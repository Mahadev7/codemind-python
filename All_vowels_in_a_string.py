a=input()
b=[]
c='aeiou'
s=0
for i in a:
    if i.isalpha():
        b.append(i)
p=set(b)
for i in c:
    if i in p:
        s+=1
if s==5:
    print("True")
else:
    print("False")