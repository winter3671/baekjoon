def pac(num, times_num):
    if num == 0:
        return 1

    if num == 1:
        return times_num

    return pac(num-1, times_num * num)

N, K = map(int, input().split())
result = (pac(N, 1) // pac(N-K, 1)) // pac(K, 1)

print(result)