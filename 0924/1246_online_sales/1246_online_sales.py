N, M = map(int, input().split())
nums = list(int(input()) for _ in range(M))
nums.sort()

max_price = 0
price = 0

start = 0
if N < M:   # 만약 달걀의 개수가 인원수보다 작으면, 전체를 다 탐색할 필요가 x
            # 모든 달걀을 팔 때부터 탐색
    start = M - N

for i in range(start, M):
    if max_price < nums[i] * (M - i):   # 최대값을 갱신하면
        max_price = nums[i] * (M - i)
        price = nums[i]     # 그때 price를 재설정

print(price, max_price)