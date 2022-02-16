import heapq
import math
import sys
from collections import deque
sys.setrecursionlimit(100000)
INF = int(1e9)

if __name__ == "__main__":

    arr = list(sys.stdin.readline().rstrip('\n'))
    bomb = sys.stdin.readline().rstrip('\n')

    stack = []

    for i in arr:
        stack.append(i)
        if i == bomb[-1] and "".join(stack[-(len(bomb)):]) == bomb:
            del stack[-(len(bomb)):]

    if len(stack) != 0:
        print("".join(stack))
    else:
        print("FRULA")