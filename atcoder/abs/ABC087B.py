A_500 = int(input())
B_100 = int(input())
C_50  = int(input())
X = int(input())

r = set()
for a in range(A_500 + 1):
    for b in range(B_100 + 1):
        for c in range(C_50 + 1):
            if X == (a * 500) + (b * 100) +(c * 50):
                r.add((a, b, c))
print(len(r))