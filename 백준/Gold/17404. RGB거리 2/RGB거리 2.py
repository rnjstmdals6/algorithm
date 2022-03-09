import sys

N = int(input())
RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(2)]
INF = 10 ** 6
ans = INF
for k in range(3):
    dp[0][0], dp[0][1], dp[0][2] = INF, INF, INF
    dp[0][k] = RGB[0][k]
    for i in range(1, N):
        dp[1][0] = min(dp[0][1], dp[0][2]) + RGB[i][0]
        dp[1][1] = min(dp[0][0], dp[0][2]) + RGB[i][1]
        dp[1][2] = min(dp[0][0], dp[0][1]) + RGB[i][2]

        dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]

    ans = min(ans, min(dp[0][(k + 1) % 3], dp[0][(k + 2) % 3]))

print(ans)