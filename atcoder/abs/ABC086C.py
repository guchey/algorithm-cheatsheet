N = int(input())
bt, bx, by = 0, 0, 0
r = True
for _ in range(N):
    t, x, y = map(int, input().split())
    tn, xn, yn = abs(t - bt), abs(x - bx), abs(y - by)
    if tn < xn + yn or (xn + yn) % 2 != tn % 2:
        print('No')
        exit()
    bt, bx, by = t, x, y
print('Yes')