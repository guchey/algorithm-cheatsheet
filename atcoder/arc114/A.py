from math import sqrt, gcd
from functools import reduce
from operator import mul

def I(): return int(input())
def LI(): return map(int, input().split())

def prime(value):
    i = 2
    while i <= sqrt(value):
        if value % i == 0:
            return i
        i += 1
    return value

def coprime(a, b):
    return gcd(a, b) == 1

N = I()
Xn = LI()
S = set()
for x in Xn:
    S.add(prime(x))
print(reduce(mul, S))