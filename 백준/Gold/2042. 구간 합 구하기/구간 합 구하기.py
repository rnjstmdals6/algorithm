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
    # 범위 밖
    if left > end or right < start:
        return 0
    # 범위 안
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return seg_sum(start, mid, node * 2, left, right) + seg_sum(mid + 1, end, node * 2 + 1, left, right)

# index : 구간 합을 수정하고자 하는 노드 dif : 수정할 값
def seg_update(start, end, node, index, dif):
    if index < start or index > end:
        return
    tree[node] += dif
    if start != end:
        mid = (start + end) // 2
        seg_update(start, mid, node * 2, index, dif)
        seg_update(mid + 1, end, node * 2 + 1, index, dif)

N, M, K = map(int, input().split())
tree = [0] * 3000000
l = []

for _ in range(N):
    l.append(int(input().rstrip()))

seg_init(0, N-1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().rstrip().split())
    # update
    if a == 1:
        b = b - 1
        dif = c - l[b]
        l[b] = c
        seg_update(0, N - 1, 1, b, dif)
    # sum
    elif a == 2:
        print(seg_sum(0, N-1, 1, b-1, c-1))