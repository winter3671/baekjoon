import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(int(input()) for _ in range(N))

w = [0] * (N + 1)

if N <= 2:
    result = sum(nums)

elif N == 3:
    result = max(nums[0] + nums[1], nums[1] + nums[2], nums[0] + nums[2])

else:
    w[0] = nums[0]
    w[1] = nums[0] + nums[1]
    w[2] = max(nums[0] + nums[1], nums[1] + nums[2], nums[0] + nums[2])

    for i in range(3, N):
        w[i] = max(w[i - 1], w[i-3] + nums[i - 1] + nums[i], w[i-2] + nums[i])

    result = w[N - 1]

print(result)