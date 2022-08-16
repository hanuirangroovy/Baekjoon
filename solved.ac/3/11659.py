import sys

n, m = map(int, sys.stdin.readline().strip().split())
lst_n = list(map(int, sys.stdin.readline().strip().split()))

sum_n = [0] * (n+1)
sum_n[1] = lst_n[0]
for i in range(2, n+1):
    sum_n[i] = sum_n[i-1] + lst_n[i-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(sum_n[j] - sum_n[i - 1])

