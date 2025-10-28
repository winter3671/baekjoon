'''
1. 문제 분석
두가지 종류의 체스판 중 더 적게 칠할 수 있는 체스판을 골라, 그 색칠횟수를 출력
체스판을 자를 수 있는 모든 경우를 탐색하고, 각각 체스판을 검증

2. 풀이 방법 고안
두가지 체스판 별로 각각 색칠횟수를 도출하고, min으로 출력
'''
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
min_result = float('inf')

for cut_N in range(N - 8 + 1):
    for cut_M in range(M - 8 + 1):
        cut_arr = [arr[cut_N + i][cut_M:cut_M + 8] for i in range(8)]

        result1 = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0 and cut_arr[i][j] == 'W':
                    result1 += 1
                elif (i + j) % 2 == 1 and cut_arr[i][j] == 'B':
                    result1 += 1

        result2 = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0 and cut_arr[i][j] == 'B':
                    result2 += 1
                elif (i + j) % 2 == 1 and cut_arr[i][j] == 'W':
                    result2 += 1

        min_result = min(min_result, result1, result2)

print(min_result)