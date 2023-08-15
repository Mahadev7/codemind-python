n=int(input())
for i in range(n):
    for k in range(n):
        if i==k:
            print('0',end='')
        else:
            print('x',end='')
    print()