import sys

n = int(sys.stdin.readline())
list_s = []
for i in range(n):
    w, h = map(int, sys.stdin.readline().split())
    list_s.append((w, h))

for i in list_s:
    rank = 1
    for j in list_s:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")