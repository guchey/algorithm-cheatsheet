# C
n = int(input().replace(' ', ''))
input_string = [input() for _ in range(n)]

bt, bx, by = 0, 0, 0
result = True
for string in input_string:
    t, x, y = map(int, string.split(' '))
    step = abs(x - bx) + abs(y - by)
    if step > t:
        result = False
        break
    if step % 2 != (t - bt) % 2:
        result = False
        break
    bt, bx, by = t, x, y

if result:
    print("Yes")
else:
    print("No")
