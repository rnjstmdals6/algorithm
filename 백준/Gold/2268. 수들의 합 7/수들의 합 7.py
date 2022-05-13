import math
import sys

input = sys.stdin.readline


def seg_init(start, end, node):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = seg_init(start, mid, node * 2) + seg_init(mid + 1, end, node * 2 + 1)
        return tree[node]


def seg_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    tmp = seg_sum(start, mid, node * 2, left, right) + seg_sum(mid + 1, end, node * 2 + 1, left, right)
    return tmp


def seg_update(start, end, node, index, dif):
    if index < start or index > end:
        return
    tree[node] += dif

    if start != end:
        mid = (start + end) // 2
        seg_update(start, mid, node * 2, index, dif)
        seg_update(mid + 1, end, node * 2 + 1, index, dif)


N, Q = map(int, input().split())
l = [0] * N
tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))

seg_init(0, N - 1, 1)

for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 0:
        if b <= c:
            print(seg_sum(0, N - 1, 1, b - 1, c - 1))
        else:
            print(seg_sum(0, N - 1, 1, c - 1, b - 1))
    elif a == 1:
        b = b - 1
        dif = c - l[b]
        l[b] = c
        seg_update(0, N - 1, 1, b, dif)