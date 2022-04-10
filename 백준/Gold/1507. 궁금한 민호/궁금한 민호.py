import sys

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [[1] * n for _ in range(n)]
flag = True

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or k == i:
                continue
            if a[i][j] == a[i][k] + a[k][j]:
                b[i][j] = 0
            elif a[i][j] > a[i][k] + a[k][j]:
                flag = False

ans = 0

if flag:
    for i in range(n):
        for j in range(i, n):
            if b[i][j] == 1:
                ans += a[i][j]
    print(ans)
else:
    print(-1)
