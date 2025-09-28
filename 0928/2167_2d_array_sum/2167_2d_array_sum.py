N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
K_arr = [list(map(int, input().split())) for _ in range(K)]

for i, j, x, y in K_arr:
    sum_num = 0
    for arr_i in range(i-1, x):
        for arr_j in range(j-1, y):
            sum_num += arr[arr_i][arr_j]

    print(sum_num)