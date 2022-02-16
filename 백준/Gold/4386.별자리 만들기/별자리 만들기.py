import math
import sys
from collections import deque

sys.setrecursionlimit(100000)
INF = sys.maxsize

if __name__ == "__main__":

    n = int(input())
    parent = list(range(n + 1))
    graph = []
    result = 0


    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]


    def union(a, b):
        a = find(a)
        b = find(b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b


    for i in range(1, n + 1):
        x, y = map(float, sys.stdin.readline().split())
        graph.append([x, y])

    tree = []

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            x1, y1 = graph[i - 1]
            x2, y2 = graph[j - 1]

            a = x2 - x1
            b = y2 - y1

            cost = math.sqrt((a * a) + (b * b))
            pow(cost, 3)
            tree.append([i, j, cost])

    tree.sort(key=lambda x: x[2])

    for a, b, cost in tree:
        if find(a) != find(b):
            union(a, b)
            result += cost

    print(result)
