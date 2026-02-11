'''
1. 문제 분석
산술평균, 중앙값, 최빈값, 범위를 구하시오

2. 풀이 방법 고안
파이썬에서 반올림을 할 때를 주의해서 풀어야 한다.
'''
def my_avg(num_list):
    avg = sum(num_list) / len(num_list)
    if avg >= 0:
        return int(avg + 0.5)  # 0.5를 더하고, 소숫점을 버림
    else:
        return int(avg - 0.5)

def my_median(num_list):
    return sorted(num_list)[len(num_list) // 2]

def my_mode(num_list):
    num_idx = [0 for _ in range(8001)]

    for num in num_list:
        num_idx[num + 4000] += 1

    mode = []
    for i in range(len(num_idx)):
        if num_idx[i] == max(num_idx):
            mode.append(i)

    if len(mode) > 1:
        return mode[1] - 4000
    else:
        return mode[0] - 4000

def my_range(num_list):
    return max(num_list) - min(num_list)

N = int(input())
arr = [int(input()) for _ in range(N)]

# 산술평균
print(my_avg(arr))
# 중앙값
print(my_median(arr))
# 최빈값
print(my_mode(arr))
# 범위
print(my_range(arr))