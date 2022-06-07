import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs(x, y, value):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    ans = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and value == graph[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    ans += 1
    return ans*ans


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
w, b = 0, 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                w += bfs(i, j, graph[i][j])
            else:
                b += bfs(i, j, graph[i][j])

print(w, b)