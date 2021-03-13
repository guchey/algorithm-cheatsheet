# F
import itertools

A, B = map(int, input().split())
S = B - A + 1

for v in itertools.permutations(range(A, B + 1)):
    print(v)