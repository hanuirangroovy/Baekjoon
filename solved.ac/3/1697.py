import sys
from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for i in (x-1, x+1, 2*x):
            if 0 <= i <= 100000 and not visited[i]: ## 순서 확인
                visited[i] = visited[x] + 1
                queue.append(i)

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100001
print(bfs(n))
