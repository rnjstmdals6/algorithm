import sys
from collections import deque

sys.setrecursionlimit(20000)

INF = sys.maxsize

if __name__ == "__main__":

    dx = [1,0,-1,0]
    dy = [0,-1,0,1]

    N = int(input())
    K = int(input())
    board = [[0] * N for _ in range(N)]

    for _ in range(K):
        ax, ay = map(int, sys.stdin.readline().split())
        board[ax - 1][ay - 1] = -1

    L = int(input())
    changes = deque()

    for _ in range(L):
        X, C = sys.stdin.readline().split()
        changes.append([int(X), C])

    time = 0
    board[0][0] = 1
    l = 1
    apple = K
    tail = deque()
    tail.append([0, 0])
    def dfs(r, c, d):
        global time, apple, l

        if changes and changes[0][0] == time:
            if changes[0][1] == 'L':
                d = (d - 1) % 4
            elif changes[0][1] == 'D':
                d = (d + 1) % 4
            changes.popleft()

        nx, ny = r + dx[d], c + dy[d]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and apple >= 0:
            tail.append([nx, ny])
            time += 1
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                tx, ty = tail.popleft()
                board[tx][ty] = 0
            elif board[nx][ny] == -1:
                board[nx][ny] = 1
                l += 1
                apple -= 1
            dfs(nx, ny, d)
        else:
            print(time + 1)
            sys.exit(0)

    dfs(0, 0, 3)