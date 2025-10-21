nums = list(map(int, input().split()))

asc = [i for i in range(1, 9)]
des = [i for i in range(8, 0, -1)]

if nums == asc:
    print('ascending')
elif nums == des:
    print('descending')
else:
    print('mixed')