import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
l, r = 1, K

while l <= r:
    mid = (l + r) // 2
    tmp = 0
    for i in range(1, N+1):
        tmp += min(mid // i, N)
    if tmp >= K:
        r = mid - 1
        ans = mid
    else:
        l = mid + 1
print(ans)