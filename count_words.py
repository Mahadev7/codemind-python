a=list(map(str,input().split()))
c=0
v='aeiou'
c='bcdfghjklmnpqrstvwxyz'
s=0
for i in a:
    i=i.lower()
    if (i[0] in v) and (i[-1] in c):
        s+=1
print(s)