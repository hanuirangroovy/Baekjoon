import sys
from heapq import heappush, heappop

tc = int(sys.stdin.readline())
heap = []

for _ in range(tc):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (-n, n))