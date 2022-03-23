import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

susi = [int(input()) for _ in range(N)]
res = 0
for i in range(N):
    ans = set()
    for j in range(k):
        ans.add(susi[(i+j) % N])
    ans.add(c)
    res = max(res, len(ans))

print(res)