import math
import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    a, b, c, d = input().split()
    b, c, d = map(int,(b, c, d))
    arr.append([a, b, c, d])

arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])