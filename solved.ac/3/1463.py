x = int(input())

data = [0] * (10**6 + 1)

# 다이나믹 프로그래밍 (보텀업)
for i in range(2, x + 1):
    data[i] = data[i-1] + 1
    if i % 2 == 0:
        data[i] = min(data[i], data[i // 2] + 1)
    if i % 3 == 0:
        data[i] = min(data[i], data[i // 3] + 1)

print(data[x])
