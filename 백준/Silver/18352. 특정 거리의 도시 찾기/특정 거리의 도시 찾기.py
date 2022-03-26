import heapq
import sys

INF = 1e9
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append([b, 1])


def dijkstra(start):
    distance = [INF] * (N + 1)
    queue = []
    heapq.heappush(queue, [0, start])
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, [cost, i[0]])
    return distance


result = dijkstra(X)
flag = False
for i in range(len(result)):
    if result[i] == K:
        print(i)
        flag = True

if not flag:
    print(-1)