import sys


def comb(n, m):
    # mCn
    ans = 1
    for i in range(n):
        ans *= m
        m -= 1
    temp = 1
    for i in range(n,0,-1):
        temp *= i

    ans = ans // temp
    return ans


n = int(input())

for i in range(n):
    N, M = map(int, sys.stdin.readline().split())
    print(comb(N, M))
