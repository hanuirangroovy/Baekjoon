import sys

def dfs(x, y, n):
    for i in range(x,x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                print("(", end="")
                dfs(x, y, n // 2)
                dfs(x, y + n // 2, n // 2)
                dfs(x + n // 2, y, n // 2)
                dfs(x + n // 2, y + n // 2, n // 2)
                print(")", end="")
                return
    if arr[x][y] == 1:
        print(1, end="")
    else:
        print(0, end="")

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip())))

dfs(0,0,n)
