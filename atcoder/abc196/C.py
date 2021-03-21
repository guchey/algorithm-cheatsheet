# C
N = int(input())
S = range(1, 1000000)
r = 0
for s in S:
    if int(str(s) + str(s)) <= N:
        r += 1
    else:
        break
print(r)