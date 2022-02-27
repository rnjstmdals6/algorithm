import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
jewel = []
bag = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    jewel.append([M, V])
for _ in range(K):
    bag.append(int(sys.stdin.readline()))
    
jewel.sort()
bag.sort()
ans = 0
temp = []

for i in bag:
    while jewel and jewel[0][0] <= i:
        heapq.heappush(temp, -jewel[0][1])
        heapq.heappop(jewel)
    if temp:
        ans += heapq.heappop(temp)
    elif not jewel:
        break

print(-ans)