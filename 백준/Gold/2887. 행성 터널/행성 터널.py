import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = list(range(n + 1))

x_arr = []
y_arr = []
z_arr = []

cost = []
for i in range(1, n+1):
    x, y, z = map(int, input().split())
    x_arr.append([x, i])
    y_arr.append([y, i])
    z_arr.append([z, i])

x_arr.sort()
y_arr.sort()
z_arr.sort()

cnt_arr = []
for i in range(1, n):
    cnt_arr.append((abs(x_arr[i][0] - x_arr[i-1][0]), x_arr[i][1], x_arr[i-1][1]))
    cnt_arr.append((abs(y_arr[i][0] - y_arr[i - 1][0]), y_arr[i][1], y_arr[i - 1][1]))
    cnt_arr.append((abs(z_arr[i][0] - z_arr[i - 1][0]), z_arr[i][1], z_arr[i - 1][1]))

cnt_arr.sort()

res = 0
ans = 0

for i in cnt_arr:
    cost, a, b = i
    if find(parent, a) != find(parent, b):
        union(a, b)
        ans += cost
        res += 1
    if res == n:
        break

print(ans)