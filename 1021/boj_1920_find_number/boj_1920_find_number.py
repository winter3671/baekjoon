N = int(input())
N_set = set(map(int, input().split()))
M = int(input())
M_lst = list(map(int ,input().split()))

for num in M_lst:
    if num in N_set:
        print(1)
    else:
        print(0)