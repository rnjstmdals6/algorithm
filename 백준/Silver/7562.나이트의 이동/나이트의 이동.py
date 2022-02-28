import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(a):
    x, y = a
    queue = deque()
    queue.append([x, y, 0])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    while queue:
        x, y, cnt = queue.popleft()
        if x == gx and y == gy:
            print(cnt)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny, cnt + 1])


t = int(input())
for _ in range(t):
    n = int(input())
    now = list(map(int, sys.stdin.readline().split()))
    goal = list(map(int, sys.stdin.readline().split()))
    gx, gy = goal
    bfs(now)
