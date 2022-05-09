import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def dfs(x, depth):
    visited[x] = True
    d[x] = depth
    for y in graph[x]:
        if not visited[y]:
            dfs(y, depth + 1)

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


T = int(input())
for __ in range(T):
    N = int(input())

    graph = [[] for _ in range(N + 1)]
    d = [0] * (N + 1)
    visited = [0] * (N + 1)
    parent = [0] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        parent[b] = a

    root = 0
    for i in range(1, N + 1):
        if parent[i] == 0:
            root = i
            break

    dfs(root, 0)

    a, b = map(int, input().split())
    print(lca(a, b))