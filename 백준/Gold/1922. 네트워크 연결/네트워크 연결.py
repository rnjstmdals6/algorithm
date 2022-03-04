import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V = int(input())
E = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])
parent = list(range(V + 1))
ans = 0

for a, b, cost in graph:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans += cost

print(ans)