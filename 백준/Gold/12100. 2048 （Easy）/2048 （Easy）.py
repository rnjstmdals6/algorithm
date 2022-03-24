import sys
from collections import deque
import copy
input = sys.stdin.readline

def right(graph):
    for i in range(N):
        idx = N - 1
        for j in range(N - 2, -1, -1):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0
                if graph[i][idx] == 0:
                    graph[i][idx] = temp
                elif graph[i][idx] == temp:
                    graph[i][idx] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    graph[i][idx] = temp
    return graph

def down(graph):
    for j in range(N):
        idx = N - 1
        for i in range(N - 2, -1, -1):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0
                if graph[idx][j] == 0:
                    graph[idx][j] = temp
                elif graph[idx][j] == temp:
                    graph[idx][j] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    graph[idx][j] = temp
    return graph

def left(c):
    graph = copy.deepcopy(c)
    for i in range(N):
        idx = 0
        for j in range(1, N):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0
                if graph[i][idx] == 0:
                    graph[i][idx] = temp
                elif graph[i][idx] == temp:
                    graph[i][idx] *= 2
                    idx += 1
                else:
                    idx += 1
                    graph[i][idx] = temp
    return graph

def up(graph):
    for j in range(N):
        idx = 0
        for i in range(1, N):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0
                if graph[idx][j] == 0:
                    graph[idx][j] = temp
                elif graph[idx][j] == temp:
                    graph[idx][j] = temp * 2
                    idx += 1
                else:
                    idx += 1
                    graph[idx][j] = temp
    return graph

def dfs(depth, board):
    global ans
    if depth == 5:
        ans = max(ans, max(map(max, board)))
        return

    dfs(depth+1, up(copy.deepcopy(board)))
    dfs(depth+1, right(copy.deepcopy(board)))
    dfs(depth+1, down(copy.deepcopy(board)))
    dfs(depth+1, left(copy.deepcopy(board)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, board)
print(ans)