import sys

n = int(input())

L = list((map(int, sys.stdin.readline().split())))
arr = sorted(L)

h = {}
cnt = 0
for i in arr:
    if i not in h:
        h[i] = cnt
        cnt += 1

for i in L:
    print(h[i],end=' ')