# C

N = int(input())
S = input()
Q = int(input())
l = {i: S[i] for i in range(N*2)}
reverse = False
for i in range(Q):
    T, A, B = list(map(int, input().split()))
    if T == 1:
        if reverse:
            l[A-1], l[B-1] = l[B-1], l[A-1]
        if not reverse:
            l[A-1], l[B-1] = l[B-1], l[A-1]
    if T == 2:
        reverse = not reverse
print(l)