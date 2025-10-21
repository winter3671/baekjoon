T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    if N % H == 0:
        floar = H
        room = N // H
    else:
        floar = N % H
        room = N // H + 1


    if room // 10 == 0:
        result = str(floar) + '0' + str(room)
    else:
        result = str(floar) + str(room)

    print(result)