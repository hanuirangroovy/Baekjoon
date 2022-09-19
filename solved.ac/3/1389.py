import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

users = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    users[a].append(b)
    users[b].append(a)

result = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    q = deque([i])
    visited[i] = 1
    while q:
        now = q.popleft()
        for j in users[now]:
            if not visited[j]:
                visited[j] = visited[now] + 1
                q.append(j)

    result.append(sum(visited))

print(result.index(min(result))+1)