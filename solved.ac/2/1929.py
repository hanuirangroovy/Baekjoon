import sys
# import math

# def is_pn(x):
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#     return True

# n, m = map(int, sys.stdin.readline().split())
# num = 1000000
# arr = [True for i in range(num+1)]
#
# for i in range(2, int(math.sqrt(num))+1):
#     if arr[i] == True:
#         j = 2
#         while i * j <= num:
#             arr[i*j] = False
#             j += 1
#
# for i in range(n, m+1):
#     if arr[i]:
#         print(i)


n, m = map(int, sys.stdin.readline().split())
for i in range(n, m+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            break
    else:
        print(i)
