import sys
import re
from collections import deque
from itertools import permutations

INF = sys.maxsize

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        case = []
        for i in range(n):
            case.append(list(map(int, sys.stdin.readline().split())))
        case.sort()
        Max = case[0][1]
        cnt = 1
        for i in range(1, n):
            if Max > case[i][1]:
                cnt += 1
                Max = case[i][1]
        print(cnt)