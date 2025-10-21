N = int(input())
nums_set = set()
for _ in range(N):
    nums_set.add(int(input()))

nums_lst = list(nums_set)
nums_lst.sort()

for num in nums_lst:
    print(num)