N, M = map(int, input().split())
nums = list(map(int, input().split()))

result = 1
for num in nums:
    result = (result * num) % M

print(result)