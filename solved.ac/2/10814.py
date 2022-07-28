# def sort_age(data):
#     return data[0]
#
# n = int(input())
# list_m = []
# for i in range(n):
#     age, name = map(str, input().split())
#     list_m.append((age, name))
# result = sorted(list_m, key=sort_age)
#
# for i in range(n):
#     print(result[i][0], result[i][1])

n = int(input())
list_m = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    list_m.append((age, name))

list_m.sort(key = lambda x : x[0])

for i in list_m:
    print(i[0], i[1])