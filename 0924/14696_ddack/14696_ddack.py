N = int(input())
for _ in range(N):
    a_nums = list(map(int, input().split()))
    b_nums = list(map(int, input().split()))
    a = a_nums[0]
    a_list = a_nums[1:]
    b = b_nums[0]
    b_list = b_nums[1:]

    a_idx = [0] * 5
    b_idx = [0] * 5

    for num in a_list:
        a_idx[num] += 1
    for num in b_list:
        b_idx[num] += 1

    for i in range(4, -1, -1):
        if a_idx[i] > b_idx[i]:
            print('A')
            break

        elif a_idx[i] < b_idx[i]:
            print('B')
            break

    else:
        print('D')
