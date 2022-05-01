import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
k = 1
for i in range(1, N + 1):
    if i == k ** 2:
        dp[i] = 1
        k += 1
    else:
        dp[i] = i
        for j in range(1, k):
            dp[i] = min(dp[i - j**2]+1, dp[i])

print(dp[N])