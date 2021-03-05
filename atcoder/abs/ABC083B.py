N, A, B = map(int, input().split())
r = 0
for n in range(1, N+1):
    if A <= sum(map(int, str(n))) <= B:
        r = r + n
print(r)
