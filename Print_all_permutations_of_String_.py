from itertools import permutations
a=input()
w=[''.join(i) for i in permutations(a)]
for i in w:
    print(i)