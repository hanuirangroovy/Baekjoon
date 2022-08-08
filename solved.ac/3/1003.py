import sys

# 시간 초과
# def fibonacci(n):
#     if n == 0:
#         result[0] += 1
#         return 0
#     elif n == 1:
#         result[1] += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    len_z = len(result_z)
    if n >= len_z:
        for i in range(len_z, n+1):
            result_z.append(result_z[i-1] + result_z[i-2])
            result_one.append(result_one[i-1] + result_one[i-2])

tc = int(sys.stdin.readline())
for _ in range(tc):
    result_z = [1,0,1]
    result_one = [0,1,1]
    n = int(sys.stdin.readline())
    fibonacci(n)
    print(result_z[n], result_one[n])