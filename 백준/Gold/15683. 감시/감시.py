import sys
import copy

input = sys.stdin.readline


# CCTV
def cctv1(board, x, y, i):
    while 0 <= x < N and 0 <= y < M and board[x][y] != 6:
        if board[x][y] == '#':
            x += dx1[i]
            y += dy1[i]
            continue
        if not (0 < board[x][y] <= 5):
            board[x][y] = '#'
        x += dx1[i]
        y += dy1[i]


def cctv2(board, x, y, i):
    nx, ny = x, y
    while 0 <= x < N and 0 <= y < M and board[x][y] != 6:
        if board[x][y] == '#':
            x += dx2[i]
            y += dy2[i]
            continue
        if not (0 < board[x][y] <= 5):
            board[x][y] = '#'
        x += dx2[i]
        y += dy2[i]
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == '#':
            nx -= dx2[i]
            ny -= dy2[i]
            continue
        if not (0 < board[nx][ny] <= 5):
            board[nx][ny] = '#'
        nx -= dx2[i]
        ny -= dy2[i]


def cctv3(board, x, y, i):
    nx, ny = x, y
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == '#':
            nx += dx3[i]
            continue
        if not (0 < board[nx][ny] <= 5):
            board[nx][ny] = '#'
        nx += dx3[i]
    while 0 <= x < N and 0 <= y < M and board[x][y] != 6:
        if board[x][y] == '#':
            y += dy3[i]
            continue
        if not (0 < board[x][y] <= 5):
            board[x][y] = '#'
        y += dy3[i]


def cctv4(board, x, y, i):
    nx, ny = x, y
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == '#':
            nx += dx2[i]
            ny += dy2[i]
            continue
        if not (0 < board[nx][ny] <= 5):
            board[nx][ny] = '#'
        nx += dx2[i]
        ny += dy2[i]
    nx, ny = x, y
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == '#':
            nx -= dx2[i]
            ny -= dy2[i]
            continue
        if not (0 < board[nx][ny] <= 5):
            board[nx][ny] = '#'
        nx -= dx2[i]
        ny -= dy2[i]
    nx, ny = x, y
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == '#':
            nx += dx1[i]
            ny += dy1[i]
            continue
        if not (0 < board[nx][ny] <= 5):
            board[nx][ny] = '#'
        nx += dx1[i]
        ny += dy1[i]


def cctv5(board, x, y):
    nx, ny = x, y
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == '#':
            nx += 1
            continue
        if not (0 < board[nx][ny] <= 5):
            board[nx][ny] = '#'
        nx += 1
    nx, ny = x, y
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == '#':
            nx -= 1
            continue
        if not (0 < board[nx][ny] <= 5):
            board[nx][ny] = '#'
        nx -= 1
    nx, ny = x, y
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == '#':
            ny += 1
            continue
        if not (0 < board[nx][ny] <= 5):
            board[nx][ny] = '#'
        ny += 1
    nx, ny = x, y
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == '#':
            ny -= 1
            continue
        if not (0 < board[nx][ny] <= 5):
            board[nx][ny] = '#'
        ny -= 1


def dfs(depth, board):
    global result
    if depth == len(arr):
        ans = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    ans += 1
        result = min(result, ans)
        return
    else:
        temp = copy.deepcopy(board)
        nx, ny = arr[depth]
        if temp[nx][ny] == 1:
            for i in range(4):
                cctv1(temp, nx, ny, i)
                dfs(depth+1, temp)
                temp = copy.deepcopy(board)
        elif temp[nx][ny] == 2:
            for i in range(2):
                cctv2(temp, nx, ny, i)
                dfs(depth+1, temp)
                temp = copy.deepcopy(board)
        elif temp[nx][ny] == 3:
            for i in range(4):
                cctv3(temp, nx, ny, i)
                dfs(depth + 1, temp)
                temp = copy.deepcopy(board)
        elif temp[nx][ny] == 4:
            for i in range(4):
                cctv4(temp, nx, ny, i)
                dfs(depth + 1, temp)
                temp = copy.deepcopy(board)
        elif temp[nx][ny] == 5:
            cctv5(temp, nx, ny)
            dfs(depth + 1, temp)
            temp = copy.deepcopy(board)


N, M = map(int, input().split())
graph = []
result = 1e9
arr = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if 0 < graph[i][j] <= 5:
            arr.append([i, j])

dx1, dy1 = [-1, 0, 1, 0], [0, 1, 0, -1]
dx2, dy2 = [0, 1, 0, 1], [1, 0, 1, 0]
dx3, dy3 = [-1, 1, 1, -1], [1, 1, -1, -1]

dfs(0, graph)
print(result)
