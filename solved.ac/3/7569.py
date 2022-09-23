from collections import deque
import sys

def tomato():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx >= 0 and nx < h and ny >= 0 and ny < n and nz >= 0 and nz < m and graph[nx][ny][nz] == 0:
                q.append([nx,ny, nz])
                graph[nx][ny][nz] = graph[x][y][z] + 1

m, n, h = map(int, sys.stdin.readline().split())
graph = []
result = 0
result_ripen = 0
result_unripen = 0
q = deque([])
for i in range(h):
    list_tomato = []
    for j in range(n):
        list_tomato.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if list_tomato[j][k] == 1:
                q.append([i,j,k])
    graph.append(list_tomato)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                result_ripen += 1

tomato()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                result_unripen += 1
            else:
                result = max(result, graph[i][j][k])

if result_ripen == n*m*h:
    print(0)
elif result_unripen > 0:
    print(-1)
else:
    print(result-1)