import sys
from collections import deque

INF = 1e9
input = sys.stdin.readline

N, M = map(int, input().split())
q = deque(list(range(1, N+1)))
s = list(map(int, input().split()))
cnt = 0
for i in s:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) > (len(q) / 2):
                q.appendleft(q.pop())
            else:
                q.append(q.popleft())
            cnt += 1
print(cnt)