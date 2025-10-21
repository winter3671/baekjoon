N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

N_idx = [0] * 20000001
for i in N_lst:
    N_idx[i+10000000] += 1

for i in M_lst:
    print(N_idx[i+10000000], end='\n')