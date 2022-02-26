import copy
import itertools
import sys
from collections import deque
sys.setrecursionlimit(20000)
INF = sys.maxsize

dx = [-1,-1,-1, 1, 1, 1, 0, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    S[x][y] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < c and 0 <= ny < r and S[nx][ny] == 1:
                S[nx][ny] = -1
                queue.append([nx, ny])

while True:
    r, c = map(int, sys.stdin.readline().split())
    if r == 0 and c == 0:
        break
    S = [list(map(int, sys.stdin.readline().split())) for _ in range(c)]

    cnt = 0

    for i in range(c):
        for j in range(r):
            if S[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)