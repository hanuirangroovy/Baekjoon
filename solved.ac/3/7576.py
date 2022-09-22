from collections import deque
import sys

def tomato():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                q.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1

m, n = map(int, sys.stdin.readline().split())
graph = []
result = 0
result_zero = 0
q = deque([])
for i in range(n):
    graph.append(list(sys.stdin.readline().strip().split()))
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

tomato()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result_zero = -1
        else:
            result = max(result, graph[i][j])

if result_zero == -1:
    print(result_zero)
else:
    print(result)






for i in range(n):
    for j in range(m):
        tomato(i,j)

print(graph)