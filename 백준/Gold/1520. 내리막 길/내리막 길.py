import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dp = [[-1] * M for _ in range(N)]


def dfs(x, y):
    if x == N - 1 and y == M - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0, 0))