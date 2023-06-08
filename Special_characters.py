n=input()
x,y,z=[],[],[]
for i in n:
    if not i.isalnum():
        x.append(i)
    elif i.isdigit() and int(i)%2==0:
        y.append(i)
    elif i.isdigit() and int(i)%2!=0:
        z.append(i)
p=len(x)
s=[]
while 1:
    if p%2==0:
        if len(y)==0 and len(z)==0:
            break
        elif len(z)==0:
            s.append(y[0])
            y.pop(0)
        elif len(y)==0:
            s.append(z[0])
            z.pop(0)
        else:
            s.append(y[0])
            s.append(z[0])
            y.pop(0)
            z.pop(0)
    else:
        if len(z)==0 and len(y)==0:
            break
        elif len(y)==0:
            s.append(z[0])
            z.pop(0)
        elif len(z)==0:
            s.append(y[0])
            y.pop(0)
        else:
            s.append(z[0])
            s.append(y[0])
            z.pop(0)
            y.pop(0)
q=''.join(s)
print(q)
        