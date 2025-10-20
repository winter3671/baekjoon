'''
1. 문제 분석
245의 분해합은 256(245 + 2+4+5)
100*a + 10*b + 1*c에서
101*a + 11*b + 2*c로 바꿈
'''
N = int(input())
len_N = len(str(N))
first_N = str(N)[0]
for num in range(N - ((len_N-1)*9 + int(first_N)), N):
    sum_num = 0
    for i in str(num):
        sum_num += int(i)
    if num + sum_num == N:
        print(num)
        break

else:
    print(0)