n = int(input())

if n > 1:
    for i in range(2,int(n/2)+1):
        if (n% i == 0):
            print("not a prime")
            break
    else:
        print("prime")
# If the number is less than 1 it can't be Prime
#else:
 #   print(n,"is not a Prime number")
