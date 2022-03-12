import heapq
import sys

INF = int(1e9)

# 노드 간선의 개수
V, E = map(int, sys.stdin.readline().split())
# 시작 노드번호
K = int(input())
graph = [[] for i in range(V + 1)]
distance = [INF] * (V + 1)

# u에서 v로 가는 가중치 w인 간선이 존재
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dikstra(start):
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

dikstra(K)

for i in range(1, V + 1):
    #도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INF")
    #도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])