import itertools
import sys
from collections import deque
sys.setrecursionlimit(20000)
INF = sys.maxsize

if __name__ == "__main__":

    nan = []
    result = []
    dap = []
    for i in range(9):
        nan.extend([int(input())])

    for i in itertools.combinations(nan, 7):
        _sum = 0
        for j in i:
            _sum += j
        if _sum == 100:
            result = i
            break

    for i in result:
        dap.append(i)
    dap.sort()
    for i in dap:
        print(i)