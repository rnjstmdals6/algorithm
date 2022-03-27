import heapq
import sys
from collections import deque

N = int(input())
M = int(input())
graph = [[] for i in range(N + 1)]
INF = int(1e9)
distance = [INF] * (N + 1)
for i in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

start, end = map(int, sys.stdin.readline().split())

queue = []
heapq.heappush(queue, (0, start))
distance[start] = 0

while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0]))

print(distance[end])

