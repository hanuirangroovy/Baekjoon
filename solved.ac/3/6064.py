import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    m, n, x, y = map(int, sys.stdin.readline().split())
    result = 0

    while x != y:
        if x > y:
            y += n
        elif x < y:
            x += m
        if x > m * n:
            x, y = -1, -1
            break
    print(x)