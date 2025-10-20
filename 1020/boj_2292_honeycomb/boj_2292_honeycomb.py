'''
1. 문제 분석
가운데에 1, 그 밖으로 1층당 6*층수만큼의 방이 존재
1 + 6 < 13 <= 1 + 6 + 6*2
'''
N = int(input())
std_idx = 1
std = 1
while std < N:
    std += 6*std_idx
    std_idx += 1

print(std_idx)