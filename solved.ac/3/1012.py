import sys
sys.setrecursionlimit(10**7)

def dfs(a,b):
    if a <= -1 or a >= n or b <= -1 or b >= m:
        return False
    if arr[a][b] == 1:
        arr[a][b] = 0
        dfs(a-1,b)
        dfs(a, b-1)
        dfs(a+1,b)
        dfs(a, b+1)
        return True
    return False

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    arr = [[0]*m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, sys.stdin.readline().strip().split())
        arr[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    print(result)


