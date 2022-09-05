import sys
from collections import deque

def bfs(x):
    queue = deque()
    queue.append([x])
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for i in (x-1, x+1, 2*x):
            if not visited[i] and 0 <= i <= 100001:
                visited[i] = visited[x] + 1
                queue.append(i)

n, k = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(100001)]
print(bfs(n))
