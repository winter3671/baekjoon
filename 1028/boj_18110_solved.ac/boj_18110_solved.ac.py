'''
1. 문제 분석
첫줄에 개수 n
아래에 나온 숫자들의 30% 절사평균을 구하는 문제
제외되는 사람의 수는 반올림
평균도 반올림

2. 풀이 방법 고안
파이썬에서 round()는 은행권 반올림임
my_round()를 정의해서 사용할것
'''
def my_round(num):
    return int(num + 0.5)

n = int(input())
nums = list(int(input()) for _ in range(n))
nums.sort()

if n == 0:
    print(0)
    exit()

cut = my_round(n * 15 / 100)
nums = nums[cut:n-cut]
result = sum(nums) / (n - 2 * cut)
print(my_round(result))