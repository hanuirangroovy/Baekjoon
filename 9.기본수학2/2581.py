def primenumber(n):
    if n==1:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

a = int(input())
b = int(input())
lst = []
sumV = 0
for i in range(a,b+1):
    if primenumber(i) == True:
        lst.append(i)
        sumV += i

if len(lst) == 0:
    print(-1)
else:
    minV = min(lst)
    print(sumV)
    print(minV)

