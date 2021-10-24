n = int(input())

if n == 1:
    print(n,'/',n,sep='')
# 분모+분자 값 = cnt+1 구하기
else:
    cnt = 0
    result = 0
    first_cnt = -1
    first = 0
    while n>result:
        cnt += 1
        result += cnt
        first_cnt += 1
        first += first_cnt
    #print(cnt)
    if cnt%2==0:
        up = n-first
        down = cnt+1 - up
        print(abs(up),'/',down, sep='')
    else:
        down = n-first
        up = cnt+1 - down
        print(abs(up),'/',down, sep='')
