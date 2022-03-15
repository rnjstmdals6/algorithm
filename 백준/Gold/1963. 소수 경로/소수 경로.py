import sys
from collections import deque

input = sys.stdin.readline


def sieve(m):
    flags = [0, 0] + [1] * (m - 1)
    for i in range(m + 1):
        if flags[i] == 1:
            for j in range(i * 2, m + 1, i):
                flags[j] = 0

    prime = []
    for i in range(len(flags)):
        if flags[i] == 1:
            prime.append(i)
    return prime


def bfs():
    queue = deque()
    queue.append([N, 0])
    visited[0] = True

    while queue:
        x, cnt = queue.popleft()
        now = str(x)
        if x == M:
            return cnt
        for i in range(4):
            for j in range(10):
                temp = int(now[:i] + str(j) + now[i + 1:])
                if temp in S and temp > 999 and not visited[temp]:
                    visited[temp] = True
                    queue.append([temp, cnt + 1])


S = sieve(9999)
for _ in range(int(input())):
    N, M = map(int, input().split())
    visited = [False] * 10000
    res = bfs()
    print(res if res != None else "Impossibble")
