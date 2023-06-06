q=input()
q=q.lower()
p=q.count('z')
r=q.count('o')
if 2*p==r:
    print("Yes")
else:
    print("No")