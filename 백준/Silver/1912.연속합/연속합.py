import copy
import itertools
import sys
from collections import deque
sys.setrecursionlimit(20000)
INF = sys.maxsize

n = int(input())
S = list(map(int, sys.stdin.readline().split()))

dp = [0] * n
dp[n-1] = S[n-1]

for i in range(n - 2, -1, -1):
    dp[i] = max(S[i], dp[i + 1] + S[i])

print(max(dp))