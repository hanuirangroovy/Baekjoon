n = int(input())
lst_n = list(map(int, input().split()))

lst_n.sort()

result = 0
for i in range(1, n+1):
    result += sum(lst_n[:i])

print(result)