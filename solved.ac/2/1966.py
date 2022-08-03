# import sys
# tc = int(sys.stdin.readline())
# for i in range(tc):
#     n, m = map(int,sys.stdin.readline().split())
#     list_n = list(map(int, sys.stdin.readline().split()))
#     list_t = [False] * n
#     cnt = 0
#     max_n = -1
#     num = 0
#     while list_t[m] != [True]:
#         max_n = max(list_n)
#         for j in range(n):
#             if list_n[j] == max_n:
#                 list_n[j] = -1
#                 cnt += 1
#                 num = j
#                 list_t[j] = True
#
# print(cnt)