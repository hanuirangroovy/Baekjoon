n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())
result = []
for a in range(n-7):
    for b in range(m-7):
        cnt = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if arr[0][0] == 'W':
                    if (i + j) % 2 == 1:
                        if arr[i][j] == 'B':
                            continue
                        else:
                            cnt += 1
                    else:
                        if arr[i][j] == 'W':
                            continue
                        else:
                            cnt += 1
                else:
                    if (i + j) % 2 == 1:
                        if arr[i][j] == 'W':
                            continue
                        else:
                            cnt += 1
                    else:
                        if arr[i][j] == 'B':
                            continue
                        else:
                            cnt += 1
        if cnt <= 32:
            result.append(cnt)
        else:
            result.append(64-cnt)
print(min(result))