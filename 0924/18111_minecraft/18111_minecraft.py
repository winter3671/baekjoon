# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

sum_arr = 0
max_height = 0

for i in range(N):
    for j in range(M):
        sum_arr += arr[i][j]
        if max_height < arr[i][j]:
            max_height = arr[i][j]

# 최대높이와, arr의 숫자의 총합 + B의 가능 평균 높이 비교(가지치기)
target_search = min(max_height, (sum_arr + B) // (N * M))

cnt_result = float('inf')
height_result = 0

for target_height in range(target_search, -1, -1):
    cnt = 0
    inv = B
    for i in range(N):
        for j in range(M):
            gap_block = arr[i][j] - target_height
            if gap_block > 0:   # 좌표 블록의 높이 > 목표 높이
                cnt += gap_block * 2
                inv += gap_block
            if gap_block < 0:   # 좌표 블록의 높이 < 목표 높이
                cnt += abs(gap_block)
                inv -= abs(gap_block)

    if inv >= 0:
        if cnt < cnt_result:     # 같은 경우일 때, 더 높은 높이를 찾아야 하므로 등호 X
            cnt_result = cnt
            height_result = target_height

print(cnt_result, height_result)
