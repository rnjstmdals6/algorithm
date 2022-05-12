import heapq
import sys
input = sys.stdin.readline


heap1 = [] # 최소힙
heap2 = [] # 최대힙

N = int(input())
mid = int(input())
print(mid)
for _ in range(1, N):
    a = int(input())
    if a > mid:
        heapq.heappush(heap2, a)
        if len(heap1) + 1 < len(heap2):
            heapq.heappush(heap1, (-mid, mid))
            mid = heapq.heappop(heap2)
    else:
        heapq.heappush(heap1, (-a, a))
        if len(heap2) < len(heap1):
            heapq.heappush(heap2, mid)
            mid = heapq.heappop(heap1)[1]
    print(mid)