import sys

A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())

dp = [[""] * (len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + A[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

if len(dp[-1][-1]) == 0:
    print(0)
else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])
