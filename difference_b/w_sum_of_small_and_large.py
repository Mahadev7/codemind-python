a=input()
b=a.split()
l=[]
n=[]
for i in b:
    l.append(ord(min(i)))
    n.append(ord(max(i)))
print(abs(sum(l)-sum(n)))
