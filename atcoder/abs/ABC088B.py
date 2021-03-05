N = input()
aN = list(map(int, input().split()))
Alice, Bob = 0, 0
def max_index(v):
    m = max(v)
    for i, d in enumerate(v):
        if m == d:
            return i
while True:
    Alice = Alice + aN.pop(max_index(aN))
    if not aN:
        break
    Bob = Bob + aN.pop(max_index(aN))
    if not aN:
        break
print(Alice - Bob)