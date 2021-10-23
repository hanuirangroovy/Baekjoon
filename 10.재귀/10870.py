def fibo(n):
    if n>1:
        return fibo(n-1) + fibo(n-2)
    return n
n = int(input())
print(fibo(n))