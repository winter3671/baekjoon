'''
1. 문제 분석
중요도가 가장 높지 않다면 출력 순서를 맨 뒤로 옮김
'''
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    q = deque(list(enumerate(num_lst)))
    cnt = 1
    result = 0

    while result == 0:
        print_check = False
        idx, imp = q.popleft()
        for another in q:
            another_idx, another_imp = another
            if imp < another_imp:
                break

        else:
            if idx == M:
                result = cnt
            cnt += 1
            print_check = True

        if not print_check:
            q.append((idx, imp))


    print(result)