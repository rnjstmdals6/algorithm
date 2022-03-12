import sys
import heapq
from collections import deque
input = sys.stdin.readline

def topology_sort():
    dp = [0] * (N+1)
    q = deque()

    for i in range(N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] += D[i]

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now]+D[i])

            if indegree[i] == 0:
                q.append(i)
    return dp[W]

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for i in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    W = int(input())
    print(topology_sort())