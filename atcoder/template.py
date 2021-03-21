import math
from math import ceil, e, floor, sqrt
import itertools
from functools import reduce, lru_cache
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


@lru_cache(maxsize=10000)
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


@lru_cache(maxsize=10000)
def coprime(a, b) -> bool:
    """
    互いに素
    """
    return gcd(a, b) == 1


@lru_cache(maxsize=10000)
def gcd(*v):
    """
    最大公約数
    """
    return reduce(math.gcd, v)


def _lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


@lru_cache(maxsize=10000)
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


def recursivesearch(w, v, i=None):
    """
    再帰で組み合わせを列挙
    :param w: 求めたい総和
    :param v: 配列
    :param i: 現在位置
    """
    if i is None:
        i = len(v)
    if i == 0:
        return w == 0
    if recursivesearch(w, v, i - 1):
        return True
    if recursivesearch(w - v[i - 1], v, i - 1):
        return True
    return False


@lru_cache(maxsize=10000)
def fibo(v):
    """
    フィボナッチ数列
    """
    if v == 0:
        return 0
    if v == 1:
        return 1
    return fibo(v - 1) + fibo(v - 2)


def dppush(hs):
    """
    0 -> i まで遷移するときの最小コストを動的計画法で計算する。
    遷移できるパターンとその際のコストは以下の通り
    i -> i+1 => abs(hs[i] - hs[i+1])
    i -> i+2 => abs(hs[i] - hs[i+2])

    :param hs: 0 -> i 高さの配列
    """
    N = len(hs)
    INF = 1000000000000
    dp = [INF for _ in range(N)]  # 初期化
    for i in range(N):
        if i == 0:
            dp[0] = 0  # 初期条件
        if i > 0:
            dp[i] = min(dp[i], dp[i-1] + abs(hs[i - 1] - hs[i]))
            if i > 1:
                dp[i] = min(dp[i], dp[i-2] + abs(hs[i - 2] - hs[i]))
    return dp[N - 1]


def dpknapsack(W, weight_and_value_pair):
    """
    ナップサック問題を動的計画法で計算する
    :param W: 総重量（製薬）
    :param wait_and_value_pair: (重量, 価値)
    """
    N = len(weight_and_value_pair)
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]  # 初期化
    for i in range(N):
        for j in range(W):
            weight, value = weight_and_value_pair[i]
            if j - weight >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j - weight] + value)
            dp[i][j] = max(dp[i+1][j], dp[i][j])
    return dp[N][W]
