import heapq
import sys

N, E = map(int, sys.stdin.readline().split())
INF = int(1e9)

graph = [[] for _ in range(N + 1)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start):
    distance = [INF] * (N + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance


ori_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = ori_distance[v1] + v1_distance[v2] + v2_distance[N]
v2_path = ori_distance[v2] + v2_distance[v1] + v1_distance[N]

result = min(v1_path, v2_path)
print(result if result < INF else -1)