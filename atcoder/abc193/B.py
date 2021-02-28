# B
N = int(input())
m = -1
for i in range(N):
    A, P, X = map(int, input().split(' '))
    if X > A:
        if m == -1 or m > P:
            m = P
print(m)