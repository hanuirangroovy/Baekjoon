def factorial(n):
    global result
    if n > 0:
        result = n*factorial(n-1)
    return result

n = int(input())
result = 1
print(factorial(n))