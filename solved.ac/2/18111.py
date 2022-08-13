
n, m, b = map(int, input().split())
arr = []
result_time = 99999999999999999999999999999999999
result_h = 0
for _ in range(n):
    arr.append(list(map(int, input().split())))
for floor in range(257):

    for i in range(n):
        max_f = 0
        min_f = 0
        for j in range(m):
            if arr[i][j] >= floor:
                min_f += floor - arr[i][j]
            else:
                max += arr[i][j] - floor
        invent = max_f + b
        if invent < min_f:
            continue
        time = 2* max_f + min_f
        if time <= result_time:
            result_time = time
            result_h = floor
print(result_time, result_h)




