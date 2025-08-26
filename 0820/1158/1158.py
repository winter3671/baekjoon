from collections import deque

N, K = map(int, input().split())
q = deque()
nums = deque(i for i in range(1, N+1))
cnt = 1

while len(nums) > 0:
    if cnt % K != 0:
        nums.append(nums.popleft())
    else:
        q.append(nums.popleft())
    cnt += 1

print(f'<{", ".join(map(str, q))}>')