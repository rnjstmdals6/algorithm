import collections
import sys

_ = sys.stdin.readline()
N = sys.stdin.readline().split()
_ = sys.stdin.readline()
M = sys.stdin.readline().split()

C = collections.Counter(N)


for m in M:
    if m in C:
        print(1)
    else:
        print(0)