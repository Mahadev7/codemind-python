x=input()
a,b,c=[],[],[]
for i in x:
    if not i.isalnum():
        a.append(i)
    elif i.isdigit() and int(i)%2==0:
        b.append(i)
    elif i.isdigit() and int(i)%2!=0:
        c.append(i)
l=len(a)
r=[]
while True:
    if l%2==0:
        if len(b)==0 and len(c)==0:
            break
        elif len(b)==0:
            r.append(c[0])
            c.pop(0)
        elif len(c)==0:
            r.append(b[0])
            b.pop(0)
        else:
            r.append(b[0])
            r.append(c[0])
            c.pop(0)
            b.pop(0)
    else:
        if len(b)==0 and len(c)==0:
            break
        if len(c)==0:
            r.append(b[0])
            b.pop(0)
        elif len(b)==0:
            r.append(c[0])
            c.pop(0)
        else:
            r.append(c[0])
            r.append(b[0])
            b.pop(0)
            c.pop(0)
z=''.join(r)
print(z)