x, y, w, h = list(map(int,input().split()))
result = [x, y, w-x, h-y]
print(min(result))
