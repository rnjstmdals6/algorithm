import sys

N, K = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
ans = -(10**6)
end = 0
_sum = 0

for start in range(len(A) - K + 1):
    while end < N and end < start + K:
        _sum += A[end]
        end += 1
    ans = max(_sum, ans)
    _sum -= A[start]

print(ans)