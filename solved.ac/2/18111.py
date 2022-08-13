import sys

n, m, b = map(int, sys.stdin.readline().split())
arr = []
result_time = float('inf')
result_h = 0
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
for floor in range(257):
    max_f = 0
    min_f = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= floor:
                max_f += arr[i][j] - floor
            else:
                min_f += floor - arr[i][j]
    if max_f + b >= min_f:
        if (2* max_f + min_f) <= result_time:
            result_time = (2* max_f + min_f)
            result_h = floor
print(result_time, result_h)




