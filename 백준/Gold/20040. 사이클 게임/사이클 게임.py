import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().split())
parent = list(range(n))
cnt = 0
isComplete = False
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(parent, a) != find(parent, b):
        union(a, b)
        cnt += 1
    else:
        isComplete = True
        break

if isComplete:
    print(cnt+1)
else:
    print(0)