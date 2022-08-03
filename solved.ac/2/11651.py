import sys
n = int(sys.stdin.readline())
list_n = []
for i in range(n):
    list_n.append(list(map(int, sys.stdin.readline().split())))
list_n.sort(key=lambda x: (x[1], x[0]))
for xy in list_n:
    print(xy[0], xy[1])