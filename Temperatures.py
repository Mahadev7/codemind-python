n = int(input())
x = list(map(int,input().split()))
l = []
f = False
c = 1
for i in range(n):
    for j in range(i+1,n):
        if x[j] > x[i]:
            l.append(c)
            f = True
            break
        else:
            c+=1
    if f == False:
        l.append(0)
    f = False
    c = 1
print(*l)