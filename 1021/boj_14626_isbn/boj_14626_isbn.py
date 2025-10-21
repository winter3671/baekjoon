nums = input()
index = 0
sum_nums = 0
for i in range(len(nums)):
    if nums[i] in '0123456789':
        if i % 2 == 0:
            sum_nums += int(nums[i])
        else:
            sum_nums += int(nums[i]) * 3
    else:
        if i % 2 == 0:
            odd = False
        else:
            odd = True

if odd:
    for i in range(10):
        if (sum_nums + i*3) % 10 == 0:
            result = i
else:
    for i in range(10):
        if (sum_nums + i) % 10 == 0:
            result = i

print(result)