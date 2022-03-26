import heapq
import sys

INF = 1e9
input = sys.stdin.readline

def dijkstra():
    queue = []
    heapq.heappush(queue, [0, 0, 0])
    visited[0][0] = True

    while queue:
        cnt, x, y = heapq.heappop(queue)
        if x == N - 1 and y == M - 1:
            print(cnt)
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True

                if graph[nx][ny] == 1:
                    heapq.heappush(queue, [cnt+1, nx, ny])
                else:
                    heapq.heappush(queue, [cnt, nx, ny])


M, N = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
visited = [[False] * M for _ in range(N)]
dijkstra()