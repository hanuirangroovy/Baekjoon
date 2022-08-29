import sys
sys.setrecursionlimit(10**7)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1
print(cnt)

