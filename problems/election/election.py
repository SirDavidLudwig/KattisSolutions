from math import factorial as fact
import sys

def nCr(n, k):
    return fact(n)/(fact(k)*fact(n-k))

def b(x, n):
    return nCr(n, x) * (0.5**n)

for i in range(int(sys.stdin.readline())):
    n, v1, v2, w = (int(x) for x in sys.stdin.readline().split(" "))
    p = 0
    if v2 >= n/2 or (v1 == v2 and v1 + v2 == n):
        print("RECOUNT!")
    else:
        if n//2 - v1 >= 0:
            for j in range(n//2 - v1, n-v1-v2):
                p += b(j+1, n-v1-v2)
        else:
            p = 1
        if p > w*0.01:
            print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
        else:
            print("PATIENCE, EVERYONE!")
