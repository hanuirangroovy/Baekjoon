import sys

n, r, c = map(int, sys.stdin.readline().split())

result = 0

while n!=0:
    n -= 1

    if r < 2 ** n and c < 2 ** n:
        continue

    elif r < 2 ** n and c >= 2 ** n:
        result += ( 2 ** n ) * ( 2 ** n )
        c -= 2 ** n

    elif r >= 2 ** n and c < 2 ** n:
        result += ( 2 ** n ) * ( 2 ** n ) * 2
        r -= 2 ** n

    else:
        result += ( 2 ** n ) * ( 2 ** n ) * 3
        r -= 2 ** n
        c -= 2 ** n

print(result)