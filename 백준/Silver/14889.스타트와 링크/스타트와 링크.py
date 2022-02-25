import itertools
import sys
from collections import deque
sys.setrecursionlimit(20000)
INF = sys.maxsize

if __name__ == "__main__":
    N = int(input())
    S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    teams = list(itertools.combinations(list(range(N)), N // 2))
    ans = INF

    for A in teams:
        start = 0
        link = 0
        for x in A:
            for y in A:
                start += S[x][y]
        B = [b for b in range(N) if b not in A]
        for x in B:
            for y in B:
                link += S[x][y]
        ans = min(ans, abs(start-link))
    
    print(ans)
