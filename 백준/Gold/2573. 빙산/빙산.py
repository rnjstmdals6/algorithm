import sys
from copy import copy, deepcopy
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and graph[nx][ny]:
                dfs(nx, ny)

def check(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not graph[nx][ny]:
            temp[x][y] += 1

N, M = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
graph = [list(map(int, input().split())) for _ in range(N)]
years = 0

while True:
    # 빙산 개수 체크
    nums = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                nums += 1

    if nums == 0:
        print(0)
        break
    elif nums >= 2:
        print(years)
        break

    # 빙산 녹임
    temp = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                check(i, j)

    for i in range(N):
        for j in range(M):
            graph[i][j] -= temp[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    years += 1