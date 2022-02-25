import itertools
import sys
from collections import deque
INF = sys.maxsize

if __name__ == "__main__":

    E, S, M = map(int,sys.stdin.readline().split())
    cnt = 0
    e, s, m = 0, 0, 0


    while True:
        if [e, s, m] != [E - 1, S - 1, M - 1]:
            e = ((e + 1) % 15)
            s = ((s + 1) % 28)
            m = ((m + 1) % 19)
            cnt += 1
        else:
            cnt += 1
            print(cnt)
            sys.exit(0)