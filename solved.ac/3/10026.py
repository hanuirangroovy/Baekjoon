import sys
sys.setrecursionlimit(1000000)

def dfs_color(x,y):
    visited[x][y] = True
    for dir in range(4):
        nx = x + dir_x[dir]
        ny = y + dir_y[dir]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == False:
                if graph[nx][ny] == color:
                    dfs_color(nx,ny)

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

result_color = 0
result_colorblind = 0
visited = [[False] * n for _ in range(n)]

dir_x = [-1,1,0,0]
dir_y = [0,0,-1,1]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            color = graph[i][j]
            dfs_color(i,j)
            result_color += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            color = graph[i][j]
            dfs_color(i,j)
            result_colorblind += 1


print(result_color, result_colorblind)
