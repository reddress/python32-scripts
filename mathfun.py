import math

def factor(n):
    if n == 1:
        return [1]
    for j in range(n-1):
        i = j+2
        if n % i == 0:
            return [i] + factor(math.floor(n/i))
            #print(i)
