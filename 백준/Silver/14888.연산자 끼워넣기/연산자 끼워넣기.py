import itertools
import sys
from collections import deque
sys.setrecursionlimit(20000)
INF = sys.maxsize

if __name__ == "__main__":

    N = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    arr = list(map(int, sys.stdin.readline().split()))
    sign = []
    sign.extend(['+' for _ in range(arr[0])])
    sign.extend(['-' for _ in range(arr[1])])
    sign.extend(['*' for _ in range(arr[2])])
    sign.extend(['/' for _ in range(arr[3])])

    brut = set(itertools.permutations(sign, N - 1))

    MAX = -INF
    MIN = INF

    for i in brut:
        _sum = A[0]
        for j in range(len(i)):
            if i[j] == '+':
                _sum += A[j+1]
            elif i[j] == '-':
                _sum -= A[j+1]
            elif i[j] == '*':
                _sum *= A[j+1]
            else:
                if _sum < 0:
                    a = abs(_sum)
                    b = -(a // A[j+1])
                    _sum = b
                else:
                    _sum //= A[j+1]
        MAX = max(MAX, _sum)
        MIN = min(MIN, _sum)

    print(MAX)
    print(MIN)