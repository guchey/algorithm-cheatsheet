S = input()
T = ''
d = ['dream', 'dreamer', 'erase', 'eraser']
dd = ['dream', 'dreamer', 'erase', 'eraser']

def mp():
    for dd in d:
        if S.startswith(T + dd):
            return T + dd
    return ''

while True:
    if S in dd:
        print('YES')
        break
    dd = [di for di in dd if len(di) < len(S)]
    dd = [di for di in dd if S.startswith(di)]
    if not dd:
        print('NO')
        break
    n = []
    for di in dd:
        for i in d:
            n.append(di + i)
    dd = n
