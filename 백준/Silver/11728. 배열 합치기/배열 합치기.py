import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.extend(B)
A.sort()
print(" ".join(map(str, A)))