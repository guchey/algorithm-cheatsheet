N, Y = map(int, input().split())
def main():
    for x in range(N + 1):
        for y in range(N + 1 - x):
            z = N - x - y
            if Y == (x * 10000) + (y * 5000) + (z * 1000):
                print(x, y, z)
                return False
    return True
if main():
    print(-1, -1, -1)