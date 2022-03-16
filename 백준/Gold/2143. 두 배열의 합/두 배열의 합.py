import bisect
import sys

input = sys.stdin.readline

K = int(input())

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

_sumA = []
_sumB = []

for i in range(len(A)):
    sum = 0
    for j in range(i, len(A)):
        sum += A[j]
        _sumA.append(sum)

for i in range(len(B)):
    sum = 0
    for j in range(i, len(B)):
        sum += B[j]
        _sumB.append(sum)

ans = 0
_sumB.sort()
for i in _sumA:
    temp = K - i
    left = bisect.bisect_left(_sumB, temp)
    right = bisect.bisect_right(_sumB, temp)
    ans += right - left

print(ans)