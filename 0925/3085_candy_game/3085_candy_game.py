# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
N = int(input())
arr = [list(input()) for _ in range(N)]
max_cnt = 0

for i in range(N):
    for j in range(N-1):
        # 오른쪽의 문자와 교환
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        combo = 1
        for num in range(N - 1):
            if arr[i][num] == arr[i][num + 1]:
                combo += 1
                if max_cnt < combo:
                    max_cnt = combo
            else:
                combo = 1

        combo = 1
        for num in range(N - 1):
            if arr[num][j] == arr[num + 1][j]:
                combo += 1
                if max_cnt < combo:
                    max_cnt = combo
            else:
                combo = 1

        combo = 1
        for num in range(N - 1):
            if arr[num][j + 1] == arr[num + 1][j + 1]:
                combo += 1
                if max_cnt < combo:
                    max_cnt = combo
            else:
                combo = 1

        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

for j in range(N):
    for i in range(N-1):
        # 오른쪽의 문자와 교환
        arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        combo = 1
        for num in range(N - 1):
            if arr[num][j] == arr[num+1][j]:
                combo += 1
                if max_cnt < combo:
                    max_cnt = combo
            else:
                combo = 1

        combo = 1
        for num in range(N - 1):
            if arr[i][num] == arr[i][num + 1]:
                combo += 1
                if max_cnt < combo:
                    max_cnt = combo
            else:
                combo = 1

        combo = 1
        for num in range(N - 1):
            if arr[i + 1][num] == arr[i + 1][num + 1]:
                combo += 1
                if max_cnt < combo:
                    max_cnt = combo
            else:
                combo = 1

        arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(max_cnt)