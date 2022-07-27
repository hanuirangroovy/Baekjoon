n, m = map(int,input().split())
list_n = []
for i in range(1,n+1):
    if n % i == 0:
        list_n.append(i)
list_m = []
for i in range(1,m+1):
    if m % i == 0:
        list_m.append(i)
max_nm = 0
for i in list_n:
    for j in list_m:
        if i == j:
            if i >= max_nm:
                max_nm = i
min_nm = max_nm * (n//max_nm) * (m//max_nm)

print(max_nm)
print(min_nm)