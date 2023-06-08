from itertools import permutations
n=input()
for i in permutations(n):
    b=''.join(i)
    print(b)