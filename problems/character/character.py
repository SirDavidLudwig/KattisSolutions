import operator as op
import sys

def nCr(n, k):
    if(k > n - k):
        k = n - k
    res = 1
    for i in range(k):
        res *= (n - i)
        res /= (i + 1)
    return int(res)

relationships = 0
n = int(input())
for i in range(2, n+1):
	relationships += nCr(n, i)
print(relationships)
