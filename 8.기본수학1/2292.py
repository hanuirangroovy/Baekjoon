n = int(input())
# cnt = 0 시간초과
# for i in range(n//6+1):
#     if n >= 1+6*i:
#         cnt += 1
#     else:
#         print(cnt)
#         break
cnt = 0
if n == 1:
    print(1)
else:
    while n>1:
        n = n - (6*cnt)
        cnt += 1
    print(cnt)