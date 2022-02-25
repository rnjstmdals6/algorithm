import copy
import itertools
import sys
from collections import deque
sys.setrecursionlimit(20000)
INF = sys.maxsize

if __name__ == "__main__":
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(i, j, k):
        queue = deque()
        queue.append([i, j])

        while queue:
            x, y = queue.popleft()
            visited[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and k < S[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True


    N = int(input())
    S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    S_min = min(map(min, S))
    S_max = max(map(max, S))
    result = 1

    for k in range(S_min, S_max + 1):
        visited = [[False] * N for _ in range(N)]
        temp = 0
        for i in range(N):
            for j in range(N):
                if k < S[i][j] and not visited[i][j]:
                    temp += 1
                    bfs(i, j, k)
        result = max(result, temp)

    print(result)