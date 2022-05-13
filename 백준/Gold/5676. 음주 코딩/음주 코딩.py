import math
import sys

input = sys.stdin.readline


def seg_init(start, end, node):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = seg_init(start, mid, node * 2) * seg_init(mid + 1, end, node * 2 + 1)
        return tree[node]


def seg_mul(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    tmp = seg_mul(start, mid, node * 2, left, right) * seg_mul(mid + 1, end, node * 2 + 1, left, right)
    return tmp


def seg_update(start, end, node, index, dif):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = dif
    else:
        mid = (start + end) // 2
        seg_update(start, mid, node * 2, index, dif)
        seg_update(mid + 1, end, node * 2 + 1, index, dif)
        tree[node] = tree[node * 2] * tree[node * 2 + 1]

while True:
    try:
        N, K = map(int, input().split())
        Arr = list(map(int, input().split()))
        l = []
        for arr in Arr:
            if arr > 0:
                l.append(1)
            elif arr < 0:
                l.append(-1)
            else:
                l.append(0)
        result = ''
        tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))
        seg_init(0, N - 1, 1)

        for _ in range(K):
            a, b, c = input().split()
            b = int(b)
            c = int(c)
            if a == 'C':
                if c > 0:
                    c = 1
                elif c < 0:
                    c = -1
                else:
                    c = 0

                seg_update(0, N - 1, 1, b - 1, c)
            elif a == 'P':
                x = seg_mul(0, N - 1, 1, b - 1, c - 1)
                if x == 0:
                    result += '0'
                elif x > 0:
                    result += '+'
                else:
                    result += '-'
        print(result)
    except Exception:
        break
