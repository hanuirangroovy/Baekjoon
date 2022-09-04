import sys

def route(num):
    for i in range(n):
        if visited[i] == 0 and arr[num][i] == 1:
            visited[i] = 1
            route(i)

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    visited = [0 for i in range(n)]
    route(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

## https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             if arr[j][k] == 1 or (arr[j][i]== 1 and arr[i][k]==1):
#                 arr[j][k] = 1
# for i in arr:
#     for j in i:
#         print(j, end = " ")
#     print()