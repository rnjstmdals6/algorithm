import sys
input = sys.stdin.readline

def sieve(m):
    flags = [0, 0] + [1] * (m - 1)
    for i in range(m + 1):
        if flags[i] == 1:
            for j in range(i*2, m+1, i):
                flags[j] = 0

    prime = []
    for i in range(len(flags)):
        if flags[i] == 1:
            prime.append(i)
    return prime

n = int(input())
S = sieve(n)
end = 0
_sum = 0
cnt = 0
for start in range(len(S)):
    while _sum < n and end < len(S):
        _sum += S[end]
        end += 1
    if _sum == n:
        cnt += 1

    _sum -= S[start]
    start += 1

print(cnt)