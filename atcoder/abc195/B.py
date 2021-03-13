# B
import math
A, B, W = map(int, input().split())
_max = math.ceil((W * 1000) / A)
_min = math.ceil((W * 1000) / B)
r1 = -1
r2 = 9999999
for i in range(_min, _max + 1):
    c = (W * 1000) / i
    if A <= c <= B:
        if r1 < i:
            r1 = i
        if r2 > i:
            r2 = i
if r1 != -1 and r2 != 9999999:
    print(r2, r1)
else:
    print('UNSATISFIABLE')