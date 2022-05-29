n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1][y - 1], graph[y - 1][x - 1] = 1, 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][k] and graph[k][j]:
                if graph[i][j] == 0:
                    graph[i][j] = graph[i][k] + graph[k][j]
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 10000000000

for i in range(n):
    sum = 0
    for j in range(n):
        sum += graph[i][j]
    if result > sum:
        result = sum
        mini = i
print(mini + 1)