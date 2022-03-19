import sys
input = sys.stdin.readline

x = int(input())

# x : 23
# 64 -> 32 32 -> 32 -> 16 16 -> 16 8 8 -> 16 8 4 4 -> 16 8 4 2 2 -> 16 8 4 2 1 1
# 16 8 4 2 1 0.5 0.5
arr = [64, 32, 16, 8, 4, 2, 1, 1]
cur = 0
cnt = 0
while x != 0:
    if arr[cur] > x:
        cur += 1
        continue
    x -= arr[cur]
    cnt += 1

print(cnt)