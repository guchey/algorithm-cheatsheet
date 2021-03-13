import math
import itertools

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

def isprime(value):
    for i in range(2,int(math.sqrt(value))):
        if value%i==0:
            return False
    return True