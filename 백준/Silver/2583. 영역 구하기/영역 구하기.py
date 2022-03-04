import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    S[x][y] = 1
    area = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and S[nx][ny] == 0:
                S[nx][ny] = 1
                area += 1
                queue.append([nx, ny])
    return area
M, N, K = map(int, sys.stdin.readline().split())
S = [[0] * N for _ in range(M)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
result = []
for _ in arr:
    y1, x1, y2, x2 = _
    x1 = M - x1
    x2 = M - x2

    for i in range(x2, x1):
        for j in range(y1, y2):
            S[i][j] = 1

for i in range(M):
    for j in range(N):
        if S[i][j] == 0:
            result.append(bfs(i, j))
            cnt += 1

result.sort()

print(cnt)
print(" ".join(map(str, result)))