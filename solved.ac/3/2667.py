import sys

def dfs(x,y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return cnt
    return False

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

result = 0
lst_result = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i,j) != False:
            result += 1
            lst_result.append(cnt)
lst_result.sort()
print(result)
for i in lst_result:
    print(i)