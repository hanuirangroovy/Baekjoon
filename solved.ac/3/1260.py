from collections import deque

def dfs(list_v, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in list_v[v]:
        if not visited_dfs[i]:
            dfs(list_v, i, visited_dfs)

def bfs(list_v, v, visited_bfs):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        result = queue.popleft()
        print(result, end=' ')
        for i in list_v[result]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


n, m, v = map(int, input().split())
list_v = [[] for _ in range(n+1)]
visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)
for _ in range(m):
    num_n, connect_n = map(int, input().split())
    list_v[num_n].append(connect_n)
    list_v[connect_n].append(num_n)
for i in range(len(list_v)):
    list_v[i].sort()
dfs(list_v, v, visited_dfs)
print(end="\n")
bfs(list_v, v, visited_bfs)
# print(end="\n")
# print(list_v)