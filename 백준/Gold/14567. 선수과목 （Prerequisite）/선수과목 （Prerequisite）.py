import sys
import heapq
from collections import deque
input = sys.stdin.readline

def topology():
    queue = deque()

    for i in range(N):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                result[i] = result[now] + 1
                queue.append(i)
    print(*result)

N, M = map(int, input().split())
indegree = [0] * N
result = [1] * N
graph = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    indegree[y-1] += 1

topology()