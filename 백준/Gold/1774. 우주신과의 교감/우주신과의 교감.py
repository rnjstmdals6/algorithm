import math
import sys

input = sys.stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

universe = [list(map(int, input().split())) for _ in range(N)]
path = [list(map(int, input().split())) for _ in range(M)]
parent = list(range(N + 1))

tree = []

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j:
            x1, y1 = universe[i-1]
            x2, y2 = universe[j-1]
            a, b = x2 - x1, y2 - y1
            cost = math.sqrt((a * a) + (b * b))
            tree.append([i, j, cost])

tree.sort(key=lambda x: x[2])

result = 0

for a, b in path:
    if find(a) != find(b):
        union(a, b)

for a, b, cost in tree:
    if find(a) != find(b):
        union(a, b)
        result += cost

print("{:.2f}".format(result))
