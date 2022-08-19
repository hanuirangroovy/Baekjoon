import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)
cnt = 0

for coin in coins:
    if coin <= k:
        cnt += k // coin
        k %= coin

print(cnt)