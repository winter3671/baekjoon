from collections import deque

N = int(input())
card_q = deque([i for i in range(1, N+1)])

while len(card_q) > 1:
    card_q.popleft()
    card_q.append(card_q.popleft())

result = card_q.pop()
print(result)