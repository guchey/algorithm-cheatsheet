
# B
N = int(input())
AN = list(map(int, input().split()))
BN = list(map(int, input().split()))
xfrom = -1
xto = 1001
for i in range(N):
    if xfrom < AN[i]:
        xfrom = AN[i]
    if xto > BN[i]:
        xto = BN[i]
if xfrom <= xto:
    print(xto - xfrom + 1)
else:
    print(0)
