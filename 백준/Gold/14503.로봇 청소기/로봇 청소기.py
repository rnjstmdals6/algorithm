import sys
sys.setrecursionlimit(2500)

INF = sys.maxsize

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    cnt = 0
    result = 0

    def dfs(r, c, d):
        global result, cnt

        if 0 <= r < n and 0 <= c < m and board[r][c] == 0:
            board[r][c] = -1
            cnt = 0
            result += 1

        if cnt == 4:
            if d == 2 and 0 <= r - 1 < n and board[r - 1][c] != 1:
                cnt = 0
                dfs(r - 1, c, 2)
            elif d == 3 and 0 <= c + 1 < m and board[r][c + 1] != 1:
                cnt = 0
                dfs(r, c + 1, 3)
            elif d == 1 and 0 <= c - 1 < m and board[r][c - 1] != 1:
                cnt = 0
                dfs(r, c - 1, 1)
            elif d == 0 and 0 <= r - 1 < n and board[r + 1][c] != 1:
                cnt = 0
                dfs(r + 1, c, 0)
            else:
                print(result)
                sys.exit(0)

        cnt += 1

        if d == 0:
            if 0 <= c - 1 < m and board[r][c - 1] == 0:
                dfs(r, c - 1, 3)
            else:
                dfs(r, c, 3)
        elif d == 3:
            if 0 <= r + 1 < n and board[r + 1][c] == 0:
                dfs(r + 1, c, 2)
            else:
                dfs(r, c, 2)
        elif d == 2:
            if 0 <= c + 1 < m and board[r][c + 1] == 0:
                dfs(r, c + 1, 1)
            else:
                dfs(r, c, 1)
        else:
            if 0 <= r - 1 < n and board[r - 1][c] == 0:
                dfs(r - 1, c, 0)
            else:
                dfs(r, c, 0)

    dfs(r, c, d)