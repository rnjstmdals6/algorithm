import sys
from collections import deque

test = int(input())

for i in range(test):
    n, m = map(int,sys.stdin.readline().split())

    queue = deque(list(map(int, sys.stdin.readline().split())))
    L = deque([0] * len(queue))
    L[m] = 'key'
    order = 0

    while True:
        if max(queue) == queue[0]:
            order += 1

            if L[0] == 'key':
                print(order)
                break
            else:
                queue.popleft()
                L.popleft()
        else:
            queue.append(queue.popleft())
            L.append(L.popleft())