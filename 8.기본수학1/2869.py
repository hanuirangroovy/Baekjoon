# a:up, b:down, v:tree
a,b,v = map(int, input().split())
# high = 0 시간초과
# n = 0
# while True:
#     n += 1
#     high += a
#     if high == v:
#         print(n)
#         break
#     high -= b

h = v-a
if h % (a-b) == 0:
    result = h/(a-b)
else:
    result = h/(a-b)+1
print(int(result + 1))


