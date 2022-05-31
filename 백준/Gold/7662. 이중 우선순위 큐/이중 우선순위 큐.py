import heapq
import sys

input = sys.stdin.readline


for _ in range(int(input())):
    minq = []
    maxq = []
    visited = [False] * 1000001

    for i in range(int(input())):
        x , y = input().split()
        if x == 'I':
            y = int(y)
            heapq.heappush(minq, (y,i))
            heapq.heappush(maxq, (-y,i))
            visited[i] = True
        elif x == 'D':
            if y == '-1':
                while minq and not visited[minq[0][1]]:
                    heapq.heappop(minq)
                if minq:
                    visited[minq[0][1]] = False
                    heapq.heappop(minq)
            elif y == '1':
                while maxq and not visited[maxq[0][1]]:
                    heapq.heappop(maxq)
                if maxq:
                    visited[maxq[0][1]]=False
                    heapq.heappop(maxq)

    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)

    if minq and maxq:
        print(-maxq[0][0], minq[0][0])
    else:
        print('EMPTY')