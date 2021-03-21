# A
import itertools

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N, M = map(int, input().split())
B = {}
for _ in range(N):
    S = input()
    zero = len([i for i in S if i == '0'])
    one = len(S) - zero
    d = (zero % 2 == 0, one % 2 == 0)
    B[d] = B.get(d, 0) + 1
result = 0
for b in B.values():
    if b > 1:
        c = cmb(b, 2)
        result = result + c
m = cmb(N, 2)
print(m - result)