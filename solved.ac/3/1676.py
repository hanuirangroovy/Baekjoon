import sys

n = int(sys.stdin.readline())

result = 0

while n>0:
    result += n//5
    n //= 5

print(result)