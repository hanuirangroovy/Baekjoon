import sys
from collections import deque
INF = int(1e9)

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 아기 상어 현재 크기 변수, 현재 위치 변수
now_size = 2
now_x, now_y = 0, 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            now_x, now_y = i, j
            arr[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 최단 거리 계산
def bfs():
    dist = [[-1]*n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if dist[nx][ny] == -1 and arr[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

# 먹을 물고기 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= arr[i][j] and arr[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
amount = 0

while True:
    fish_loc = find(bfs())
    if fish_loc == None:
        print(result)
        break
    else:
        now_x, now_y = fish_loc[0], fish_loc[1]
        result += fish_loc[2]
        arr[now_x][now_y] = 0
        amount += 1
        if amount >= now_size:
            now_size += 1
            amount = 0


