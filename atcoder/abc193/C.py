# C
import math

N = int(input())
sq = int(math.sqrt(N))
s = set()
for i in range(2, sq + 1):
    x = i * i
    while x <= N:
        s.add(x)
        x = x * i
print(N - len(s))