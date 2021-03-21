# E
from functools import lru_cache

N = int(input())
In = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
Xq = map(int, input().split())


@lru_cache(maxsize=10000)
def f(x, a, t):
    if t == 1:
        return x + a
    elif t == 2:
        return max(x, a)
    elif t == 3:
        return min(x, a)


for x in Xq:
    r = 0
    for (a, t) in In:
        r = f(x, a, t)
        x = r
    print(r)
