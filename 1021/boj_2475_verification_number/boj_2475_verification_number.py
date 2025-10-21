nums = list(map(int, input().split()))
sum_nums = 0
for num in nums:
    sum_nums += num**2

print(sum_nums%10)