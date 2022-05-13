import math
import sys

input = sys.stdin.readline


def seg_init(start, end, node):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = seg_init(start, mid, node * 2) * seg_init(mid + 1, end, node * 2 + 1) % 1000000007
        return tree[node]


def seg_mul(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    tmp = seg_mul(start, mid, node * 2, left, right) * seg_mul(mid + 1, end, node * 2 + 1, left, right)
    return tmp % 1000000007


def seg_update(start, end, node, index, dif):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = dif
    else:
        mid = (start + end) // 2
        seg_update(start, mid, node * 2, index, dif)
        seg_update(mid + 1, end, node * 2 + 1, index, dif)
        tree[node] = tree[node*2] * tree[node*2 + 1] % 1000000007


N, M, K = map(int, input().split())
l = []
tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))

for i in range(N):
    l.append(int(input()))

seg_init(0, N - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        seg_update(0, N - 1, 1, b-1, c)
    elif a == 2:
        print(seg_mul(0, N-1, 1, b-1, c-1))