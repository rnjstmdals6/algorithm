import math
import sys
from collections import deque
from itertools import permutations

INF = sys.maxsize

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    B.sort(reverse=True)

    result = 0
    for i in range(n):
        result += (A[i] * B[i])

    print(result)