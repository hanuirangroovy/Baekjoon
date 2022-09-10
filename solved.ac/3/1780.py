import sys

def dfs(x, y, n):
    global minusOne, zero, one
    check = arr[x][y]
    for i in range(x,x + n):
        for j in range(y, y + n):
            if arr[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * n // 3, y + l * n // 3, n // 3)
                return
    if check == -1:
        minusOne += 1
    elif check == 0:
        zero += 1
    else:
        one += 1

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

minusOne, zero, one = 0, 0, 0

dfs(0,0,n)

print(minusOne)
print(zero)
print(one)
