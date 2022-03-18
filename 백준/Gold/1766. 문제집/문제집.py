import heapq
import sys
from collections import deque

input = sys.stdin.readline


def topology():
    heap = []
    result = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        now = heapq.heappop(heap)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                heapq.heappush(heap, i)

    for i in range(len(result)):
        print(result[i], end=" ")


N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology()
