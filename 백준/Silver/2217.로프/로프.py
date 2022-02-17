import math
import sys
from collections import deque
from itertools import permutations

INF = sys.maxsize

if __name__ == "__main__":
    n = int(input())
    rope =[]

    for _ in range(n):
        w = int(input())
        rope.append(w)

    rope.sort(reverse=True)
    result = rope[0]

    for i in range(1, n):
        _sum = rope[i] * (i + 1)
        result = max(_sum, result)

    print(result)