import sys

N = int(input())
cards = [0]
cards.extend(list(map(int, sys.stdin.readline().split())))
dp = [0] * (N+1)
dp[1] = cards[1]

for i in range(2, N + 1):
    if i % 2 == 1:
        _max = -1
        a = i//2
        b = i//2 + 1
        for _ in range(i//2):
            _max = max(_max, dp[a]+dp[b])
            a -= 1
            b += 1
        dp[i] = max(_max, cards[i])
    else:
        _max = -1
        a = i//2
        b = i//2
        for _ in range(i//2):
            _max = max(_max, dp[a]+dp[b])
            a -= 1
            b += 1
        dp[i] = max(_max, cards[i])

print(dp[-1])