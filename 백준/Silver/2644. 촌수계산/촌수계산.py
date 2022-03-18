import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    queue = deque()
    queue.append([x, 0])
    visited[x] = True
    while queue:
        nx, cnt = queue.popleft()
        if nx == people[0]:
            print(cnt)
            return
        for i in graph[nx]:
            if not visited[i]:
                visited[i] = True
                queue.append([i, cnt+1])
    print(-1)
    return

n = int(input())
people = list(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(people[1])
