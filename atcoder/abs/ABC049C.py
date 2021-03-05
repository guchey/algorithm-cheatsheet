S = input()
T = ''
d = ['dream', 'dreamer', 'erase', 'eraser']

def mp():
    for dd in d:
        if S.startswith(T + dd):
            return T + dd
    return ''

while True:
    T = mp()
    if not T:
        print('NO')
        break
    if T == S:
        print('YES')
        break