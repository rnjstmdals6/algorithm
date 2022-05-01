import sys
input = sys.stdin.readline

N = input().rstrip()
M = input().rstrip()

dp = [[0] * (len(M)+1) for _ in range(len(N)+1)]
answer = 0

for i in range(1, len(N)+1):
    for j in range(1, len(M)+1):
        if N[i-1] == M[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)

print(answer)