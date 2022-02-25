import itertools
import sys
from collections import deque
sys.setrecursionlimit(20000)
INF = sys.maxsize

if __name__ == "__main__":

    def dfs(depth, idx):
        if depth == L:
            a = []
            gcnt = 0
            ccnt = 0
            for i in range(C):
                if visited[i]:
                    a.append(S[i])
                    if S[i] in gather:
                        gcnt += 1
                    else:
                        ccnt += 1
            a.sort()
            if gcnt > 0 and ccnt > 1:
                ans.append("".join(a))
            return

        for i in range(idx, C):
            if not visited[i]:
                visited[i] = True
                dfs(depth+1, i+1)
                visited[i] = False


    L, C = map(int, sys.stdin.readline().split())
    S = list(sys.stdin.readline().split())
    visited = [False for _ in range(C)]
    gather = ["a", "e", "i", "o", "u"]
    ans = []

    dfs(0, 0)
    ans.sort()
    for i in ans:
        print(i)
    # 최소 한개 모음, 최소 두개 자음, 오름차순
