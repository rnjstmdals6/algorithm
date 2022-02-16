import math
import sys
from collections import deque

sys.setrecursionlimit(100000)
INF = sys.maxsize

if __name__ == "__main__":
    n = list(map(int,list(input())))
    n.sort(reverse=True)
    
    for i in n:
        print(i, end="")