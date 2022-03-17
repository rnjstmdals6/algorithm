import bisect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(v):
    global result
    visited[v] = 1
    traced.append(v)
    
    w = s[v]
    if visited[w] == 1:
        if w in traced:
            result += traced[traced.index(w):]
            return
    else:
        dfs(w)
T = int(input())
for _ in range(T):
    n = int(input())
    s = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    result = []
    for i in range(1, n + 1):
        if visited[i] == 0:
            traced = []
            dfs(i)
    print(n - len(result))