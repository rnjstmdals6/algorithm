import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline


def dijkstra(idx):
    queue = []
    heapq.heappush(queue, [graph[0][0], 0, 0])
    visited[0][0] = True

    while queue:
        cost, x, y = heapq.heappop(queue)
        if x == N - 1 and y == N - 1:
            print("Problem", str(idx)+":", cost)
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(queue, [cost + graph[nx][ny], nx, ny])

idx = 0
while True:
    N = int(input())
    if N == 0:
        break

    idx += 1
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    dijkstra(idx)
