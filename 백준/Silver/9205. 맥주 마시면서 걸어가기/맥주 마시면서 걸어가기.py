import sys

input = sys.stdin.readline

# 모든 노드에서 다른 모든 노드까지의 최단 경로 계산
# 점화식 Dab = min(Dab , Dak + Dkb)
# 그래프를 일단 무한대로 다 초기화
T = int(input())

for __ in range(T):
    n = int(input())

    INF = int(1e9)
    graph = [[INF] * (n + 2) for _ in range(n + 2)]

    location = [list(map(int, input().split())) for _ in range(n + 2)]

    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                graph[i][j] = 0
            else:
                dis = abs(location[i][0] - location[j][0]) + abs(location[i][1] - location[j][1])
                if dis <= 1000:
                    graph[i][j] = 1

    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    if graph[0][n + 1] == INF:
        print("sad")
    else:
        print("happy")