import math
import sys

input = sys.stdin.readline
cnt = 2
n = int(input())
dp = [0] * (n+1)
dp[1] = 1

def is_sqrt(n):
    num = n ** 0.5
    if num == int(num):
        return True
    else:
        return False

for i in range(2,n+1):
    if is_sqrt(i):
        dp[i] = 1
    elif i % 2 == 0 and is_sqrt(i // 2):
        dp[i] = 2
    elif i % 3 == 0 and is_sqrt(i // 3):
        dp[i] = 3
    else:
        dp[i] = 4
        for j in range(1,int(math.sqrt(i))+1):
            dp[i] = min(dp[i], dp[j*j] + dp[i - j*j])
print(dp[n])