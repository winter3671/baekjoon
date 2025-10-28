'''
1. 문제 분석
M이상 N이하의 소수들을 모두 출력

2. 풀이 방법 고안
에라토스테네스의 체를 이용해서 소수를 구해보자
'''
M, N = map(int, input().split())
check_lst = [True for _ in range(N + 1)]
check_lst[0] = False
check_lst[1] = False

check_num = 2
while check_num <= N ** 0.5:
    if check_lst[check_num] == True:
        for i in range(check_num + 1, N+1):
            if i % check_num == 0:
                check_lst[i] = False

    check_num += 1

for idx in range(M, N+1):
    if check_lst[idx] == True:
        print(idx)