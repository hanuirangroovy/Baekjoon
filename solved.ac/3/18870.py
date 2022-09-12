import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

numbers_set = set(numbers)
numbers_sort = list(numbers_set)
numbers_sort.sort()

result = {}

for i in range(len(numbers_sort)):
    result[numbers_sort[i]] = i

for i in numbers:
    print(result[i], end=' ')
