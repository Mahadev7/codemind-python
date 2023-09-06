n = input()
p = [i for i in range(len(n)+1)]
l = []
for i in n:
    if i == 'I':
        l.append(p.pop(0))
    else:
        l.append(p.pop(-1))
l.append(p[0])
print(*l)