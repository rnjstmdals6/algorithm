import copy
import sys
from collections import deque

INF = 1e9
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    result = []
    result.append([x, y])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(A[nx][ny] - A[x][y]) <= r:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    result.append([nx, ny])
    return result


n, l, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0,0,-1,1], [-1,1,0,0]
ans = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                result = bfs(i, j)
                if len(result) > 1:
                    flag = True
                    num = sum(A[x][y] for x, y in result) // len(result)
                    for x, y in result:
                        A[x][y] = num
    if not flag:
        print(ans)
        break
    ans += 1