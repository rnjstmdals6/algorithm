import sys
input = sys.stdin.readline

A, B, C, D = [], [], [], []

n = int(input())

for _ in range(n):
    a, b, c, d = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

cnt = 0
ab = dict()
for a in A:
    for b in B:
        ab[a + b] = ab.get(a + b, 0) + 1

for c in C:
    for d in D:
        cnt += ab.get(-(c + d), 0)

print(cnt)