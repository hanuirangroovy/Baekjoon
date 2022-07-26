# 시간초과
# k, n = map(int, input().split())
# list_k = []
# result_exp = 0
# for i in range(k):
#     lin = int(input())
#     list_k.append(lin)
#     result_exp += lin
# result_exp = result_exp // n
# result = 0
# while result != n:
#     result = 0
#     for j in list_k:
#         result += (int(j) // result_exp)
#     result_exp -= 1
#
# print(result_exp+1)

# 이분탐색
k, n = map(int, input().split())
list_k = []
result_exp = 0
for i in range(k):
    list_k.append(int(input()))
start, end = 1, max(list_k)

while start <= end:
    mid = (start + end) // 2

    result = 0
    for j in list_k:
        result += j // mid

    if result >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)