import math
import sys

input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = min(init(node * 2, start, mid), init(node * 2 + 1, mid + 1, end))
    return tree[node]


def query(node, start, end, left, right):
    if start > right or end < left:
        return 10000000001
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(query(node * 2, start, mid, left, right), query(node * 2 + 1, mid + 1, end, left, right))


def init1(node, start, end):
    if start == end:
        mtree[node] = l[start]
        return mtree[node]

    mid = (start + end) // 2
    mtree[node] = max(init1(node * 2, start, mid), init1(node * 2 + 1, mid + 1, end))
    return mtree[node]


def mquery(node, start, end, left, right):
    if start > right or end < left:
        return -10000000001
    if left <= start and end <= right:
        return mtree[node]
    mid = (start + end) // 2
    return max(mquery(node * 2, start, mid, left, right), mquery(node * 2 + 1, mid + 1, end, left, right))


N, M = map(int, input().split())


l = list(int(input()) for _ in range(N))
h = int(math.ceil(math.log2(N)))
tree = [0] * (1 << (h + 1))
mtree = [0] * (1 << (h + 1))

init(1, 0, N - 1)
init1(1, 0, N - 1)

k = list(map(int, input().split()) for _ in range(M))

for a, b in k:
    print(query(1, 0, N - 1, a - 1, b - 1), mquery(1, 0, N - 1, a - 1, b - 1))