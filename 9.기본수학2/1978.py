# 1978 소수찾기

def primnumber(n):
    if n == 1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

n = int(input())

lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if primnumber(i) == True:
        cnt += 1
print(cnt)
