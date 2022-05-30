import sys

def binarySearch(S, low, high, n):
    while low <= high:
        cnt = 0
        mid = (high + low) // 2
        for i in S:
            cnt += (i // mid)
        if cnt < n:
            high = mid - 1
        elif cnt >= n:
            low = mid + 1
    return high

k, n = map(int, sys.stdin.readline().split())
S = []
for i in range(k):
    S.append(int(sys.stdin.readline()))

print(binarySearch(S, 1, max(S), n))