import itertools
import sys
from collections import deque
sys.setrecursionlimit(20000)
INF = sys.maxsize

if __name__ == "__main__":

    N, S = map(int,sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = 0

    for i in range(1, N + 1):
        for j in list(itertools.combinations(arr, i)):
            _sum = 0
            for k in j:
                _sum += k
            if _sum == S:
                cnt += 1
    print(cnt)