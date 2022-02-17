import sys
import re
from itertools import permutations

INF = sys.maxsize

if __name__ == "__main__":
    n = int(input())
    cnt = 0

    while n > cnt:
        cnt += 1
        n -= cnt
    print(cnt)