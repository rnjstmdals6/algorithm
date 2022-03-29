import sys
from collections import deque

INF = 1e9
input = sys.stdin.readline

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

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = list(range(m+1))
    
    graph = []
    
    for i in range(n):
        a, b, c = map(int, input().split())
        graph.append([a, b, c])
    
    graph.sort(key=lambda x:x[2])
    result = 0
    for a, b, cost in graph:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
        else:
            result += cost
    
    print(result)