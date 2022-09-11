import sys

def dfs(x, y, n):
    global white, blue
    check = arr[x][y]
    for i in range(x,x + n):
        for j in range(y, y + n):
            if arr[i][j] != check:
                for k in range(2):
                    for l in range(2):
                        dfs(x + k * n // 2, y + l * n // 2, n // 2)
                return
    if check == 0:
        white += 1
    else:
        blue += 1

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

white, blue = 0, 0

dfs(0,0,n)

print(white)
print(blue)