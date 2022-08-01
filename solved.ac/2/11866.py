# import sys
# n, k = map(int,sys.stdin.readline().split())
# lst_f = [False] * n
# cnt = k-1
# result = []
# while lst_f != [True]*n:
#     cnt %= n
#     if lst_f[cnt] == False:
#         lst_f[cnt] = True
#         result.append(cnt+1)
#     cnt += k
#
#
# print(result)