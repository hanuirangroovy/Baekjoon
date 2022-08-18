import sys

n, m = map(int, sys.stdin.readline().split())
set_n = set()
for _ in range(n):
    set_n.add(sys.stdin.readline().strip())

set_m = set()
for _ in range(m):
    set_m.add(sys.stdin.readline().strip())

result = sorted(list(set_n & set_m))

print(len(result))
for ans in result:
    print(ans)