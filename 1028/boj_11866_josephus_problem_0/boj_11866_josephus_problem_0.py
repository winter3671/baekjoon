'''
1. 문제 분석
N명의 사람이 원형으로 앉아있고,
K번째 사람이 제거된다.
사람이 제거되면 K-1명의 사람이 원형으로 앉아있는 모양

2. 풀이 방법 고안
원형큐를 이용하자
'''
from collections import deque

N, K = map(int, input().split())
q = [i for i in range(1, N+1)]

lev = 0
josephus = []
for i in range(N):
    lev = (lev + K) % len(q) - 1
    if lev == -1:
        lev = len(q)-1
    josephus.append(q.pop(lev))

print('<' + ", ".join(map(str, josephus)) + '>')