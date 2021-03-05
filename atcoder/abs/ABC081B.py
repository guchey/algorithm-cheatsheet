N = int(input())
A = list(map(int, input().split()))
r = 0
def even(vs):
    return all(v % 2 == 0 for v in vs)

while True:
    if not even(A):
        break
    r = r + 1
    A = [a / 2 for a in A]
print(r)