import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1


for i in range(1, N + 1):
    ans = 0
    for j in range(1, N + 1):
        if graph[i][j] != 1 and graph[j][i] != 1:
            ans += 1
    print(ans-1)
