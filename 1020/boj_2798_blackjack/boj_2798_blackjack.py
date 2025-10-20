'''
1. 문제 분석
여러 카드 중 3장을 고름
M을 넘지 않는 내에서 가장 M과 가까운 값을 출력
'''
def blackjack(start_idx, sum_num, cnt):
    global max_cards
    if cnt == 3:
        max_cards = max(max_cards, sum_num)
        return

    for i in range(start_idx, N):
        if sum_num + nums[i] > M:
            break
        blackjack(i+1, sum_num + nums[i], cnt + 1)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

max_cards = 0
blackjack(0, 0, 0)

print(max_cards)