# 시간초과
k, n = map(int, input().split())
list_k = []
for i in range(k):
    list_k.append(input())
min_k = int(min(list_k))
result = 0
while result != n:
    result = 0
    for j in list_k:
        result += (int(j) // min_k)
    min_k -= 1

print(min_k+1)