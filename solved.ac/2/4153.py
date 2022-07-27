while True:
    list_n = sorted(list(map(int,input().split())))
    if list_n[0] == 0 and list_n[1] == 0 and list_n[2] == 0:
        break
    if list_n[2]**2 == list_n[0]**2 + list_n[1]**2:
        print("right")
    else:
        print("wrong")