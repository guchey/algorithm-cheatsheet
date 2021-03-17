import math
from math import ceil, floor, sqrt
import itertools
from functools import reduce
from operator import add, sub, mul


def I(): return int(input())
def LI(): return map(int, input().split())
def S(): return input()
def LS(): return input().split()


def AND(a, b): return list(set(a) & set(b))
def OR(a, b): return list(set(a) | set(b))


def YES(): print("YES")
def NO(): print("NO")
def Yes(): print("Yes")
def No(): print("No")


def isprime(v) -> bool:
    """
    素数判定
    """
    if v == 1:
        return False
    i = 2
    while i <= sqrt(v):
        if v % i == 0:
            return False
        i += 1
    return True


def coprime(a, b) -> bool:
    """
    互いに素
    """
    return gcd(a, b) == 1


def gcd(*v):
    """
    最大公約数
    """
    return reduce(math.gcd, v)


def _lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*v):
    """
    最小公倍数
    """
    return reduce(_lcm_base, v, 1)


def bitsearch(v):
    """
    bit全探索で組み合わせを列挙
    """
    for i in range(pow(2, len(v))):
        b = []
        for j in range(len(v)):
            if (i >> j) & 1:
                b.append(v[j])
        yield b
